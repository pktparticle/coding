'''
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
O(n), easy
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=collections.Counter(nums)
        n=len(nums)//2
        for key in counter:
            if counter[key]>n:
                return key
        