# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next 
# node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = deque()
        result = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        for i in range(0, len(result)-1):
            nodex = result[i]
            nodex.left = None
            nodex.right = result[i+1]
