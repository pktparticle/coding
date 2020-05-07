'''
Problem Link:https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
O(N), Medium
'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    from collections import deque            
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level={}
        level[root.val]=0
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left:
                level.update({node.left.val: 1+level[node.val]})
                q.append(node.left)
            
            if node.right:
                level.update({node.right.val: 1+level[node.val]})
                q.append(node.right)
            if node.left and node.right:
                if (node.left.val==x and node.right.val==y) or (node.left.val==y and node.right.val==x):
                    return False
        return level[x]==level[y]