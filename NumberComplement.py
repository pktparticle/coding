'''
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
Easy, O(n)
'''


class Solution:
    def findComplement(self, num: int) -> int:
        num=list(bin(num))[2:]
        for i in range(len(num)):
            if num[i]=='1':
                num[i]='0'
            else:
                num[i]='1'
        num2=''.join(num)
        return(int(num2,2))