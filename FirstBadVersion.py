#Problem link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

#Solution:
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi=1, n
        while True:
            mid=(lo+hi)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                hi=mid-1
            else: lo=mid+1
'''
Its based on the concept of Binary Search.
'''