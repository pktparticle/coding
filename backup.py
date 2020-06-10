import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

import gspread
import mysql.connector as connector
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("users").sheet1

lower_threshold = sheet.cell(2, 5).value
upper_threshold = sheet.cell(2, 6).value

# Extracting data
#data = sheet.get_all_records()
#col = sheet.col_values(3)


class DatabaseHelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost", port="3306", user="root", password="root", database="watchtower")

        query = "CREATE TABLE IF NOT EXISTS users(uid INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, location VARCHAR(50), date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);"

        cur = self.con.cursor()
        cur.execute(query)

    def insert(self, name, location):
        query = "INSERT INTO users(name, location) VALUES('{}' , '{}')".format(
            name, location)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def query(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        res = []
        for row in cur:
            res.append(row)
        return res


# # constructor
#databaseHelper = DatabaseHelper()
# inserting data into the table

# for row in data:
#     name = row['name']
#     location = row['location']
#     databaseHelper.insert(name, location)


# querying
# query="SELECT count(uid) from users where date_joined between date_sub(current_timestamp, interval 5 minute) and current_timestamp; "
# query_res = databaseHelper.query(query)
# print(query_res)

#databaseHelper.insert('a', 'la')

"""

def mean(query_res):
    total=0
    for i in query_res:
        total+=i[0]
    avg=total/len(query_res)
    return avg

def standard_deviation(query_res, mean):
    diffSum=0
    for i in query_res:
        diffSum+=(i[0]-mean)**2
    sigma = (diffSum/len(query_res))**0.5
    return sigma

avg=mean(query_res)
sigma=standard_deviation(query_res, avg)

# threshold=1
# if avg>threshold:
#     sending_email.main()

"""


MY_ADDRESS = 'prashantt.int@homelane.com'
PASSWORD = 'prashant@homelane'


database_helper = DatabaseHelper()
query_last_hour_user_count = "SELECT count(uid) from users where date_joined between date_sub(current_timestamp, interval 60 minute) and current_timestamp;"
query_last_five_min_user_count = "SELECT count(uid) from users where date_joined between date_sub(current_timestamp, interval 5 minute) and current_timestamp;"


last_hour_user_count = database_helper.query(query_last_hour_user_count)
last_five_min_user_count = database_helper.query(
    query_last_five_min_user_count)

last_hour_avg = last_hour_user_count[0][0]/12


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():

    names, emails = get_contacts('mycontacts.txt')  # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.safe_substitute(pname=name.title(), last_hourUC=str(
            last_hour_user_count[0][0]), last_hourAvg=str(last_hour_avg), last_five_minUC=str(last_five_min_user_count[0][0]), lowerth=lower_threshold, upperth=upper_threshold)

        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Watchtower UPDATE"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        """
        The below commented code is to attach any file in the email.

        # open the file to be sent
        # rb is a flag for read-only
        filename = "myAvatar.png"
        attachment = open("myAvatar.png", "rb")

        # MIMEBase
        attac = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        attac.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(attac)

        attac.add_header('Content-Disposition',
                         "attachment; filename= %s" % filename)
        msg.attach(attac)
        """
        s.send_message(msg)

        # s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == "__main__":
    if last_hour_avg > int(lower_threshold) or last_hour_avg > int(upper_threshold):
        print("Sending email!")
        main()
