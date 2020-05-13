"""
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/
O(n), medium
"""

class Solution:
     def removeKdigits(self, num: str, k: int) -> str:
            res = []
            n = len(num)
            if n == k : return '0'

            for char in num :
                while k and res and res[-1] > char :
                    res.pop()
                    k -= 1
                res.append(char)

            while k :
                res.pop()
                k -= 1

            return ''.join(res).lstrip('0') or "0"