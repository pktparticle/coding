'''
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
Simple problem to count the total number of different types of charater in string J, that are also in string S.
'''


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter
        res=0
        for ch in J:
            res+=Counter(S)[ch]  
        return res
        