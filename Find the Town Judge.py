"""
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
Easy
"""



from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dic=defaultdict(list)
        size=len(trust)
        for i in range(size):
            dic[trust[i][0]].append(trust[i][1])
        
        nums={i for i in range(1,N+1)}
        keys=set(dic.keys())
        isJudge=nums-keys
        
        if len(isJudge)!=1: return -1
        for i in isJudge:
            isJudgeFinal=i
            break
            
        # print("nums: ", nums)
        # print("keys: ", keys)
        # print(isJudgeFinal)
        for i in dic:
            if isJudgeFinal not in dic[i]: return -1
        return isJudgeFinal
        