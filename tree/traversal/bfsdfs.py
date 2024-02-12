from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def bfs_traversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        bfs, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            bfs.append(level)
        return bfs

    def dfs_traversal(self, root: TreeNode) -> List[List[int]]:
        



# example
# tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# soln = Solution().bfs_traversal(tree)
# print(soln)
