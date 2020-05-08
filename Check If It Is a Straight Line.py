'''
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323
O(n), easy
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        flag=True
        for i in range(1,len(coordinates)):
            if coordinates[i][0]!=coordinates[i-1][0]: flag=False
        if flag: return True
        else:
            deltaY=coordinates[1][1]-coordinates[0][1]
            deltaX=coordinates[1][0]-coordinates[0][0]
            if deltaX==0: return False
            prev_slope=deltaY/deltaX
            for i in range(2, len(coordinates)):
                deltaY=coordinates[i][1]-coordinates[i-1][1]
                deltaX=coordinates[i][0]-coordinates[i-1][0]
                if deltaX==0: return False
                slope=deltaY/deltaX
                if slope!=prev_slope: return False
                else: prev_slope=slope
            return True