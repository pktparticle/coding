'''
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
Complexity: O(len(str1)+len(str2))
Easy one!
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r, s=Counter(ransomNote), Counter(magazine)
        for ch in ransomNote:
            if (ch not in s) or r[ch]>s[ch]: return False
        return True
        