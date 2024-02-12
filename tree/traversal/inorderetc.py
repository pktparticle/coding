"""
Inorder - left, root, right
Preorder - root, left, right
Postorder - left, right, root
"""
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode, li):
            if root is None:
                return None
            inorder(root.left, li)
            li.append(root.val)
            inorder(root.right, li)
            return li

        return inorder(root, [])

    def preorderTraversalRescursive(self, root: TreeNode) -> List[int]:
        def preorder(root, li):
            if root is None:
                return None
            li.append(root.val)
            preorder(root.left, li)
            preorder(root.right, li)
            return li

        return preorder(root, [])

    def postOrderTraversalRecursive(self, root: TreeNode) -> List[int]:
        def postorder(root, li):
            if root is None:
                return None
            postorder(root.left, li)
            postorder(root.right, li)
            li.append(root.val)
            return li

        return postorder(root, [])

    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        inorder, stack = [], []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                inorder.append(node.val)
                root = node.right
        return inorder

    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        preorder, stack = [], []
        while True:
            if root:
                preorder.append(root.val)
                stack.append(root)
                root = root.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                root = node.right
        return preorder

    def postorderTraversalIterative(self, root: TreeNode) -> List[int]:
        # Left, Right, Root -> reverse(Root, Right, Left)
        if root is None:
            return []
        postorder, stack = [], []
        while True:
            if root:
                postorder.append(root.val)
                stack.append(root)
                root = root.right
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                root = node.left
        return postorder[::-1]
