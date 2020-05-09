"""
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324
O(n), easy
"""



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while i*i<num:
            i+=1
        return i*i ==num
        