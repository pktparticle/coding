'''
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
O(n), easy
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=collections.Counter(s)
        for idx,ch in enumerate(s):
            if count[ch]==1: return idx
        return -1