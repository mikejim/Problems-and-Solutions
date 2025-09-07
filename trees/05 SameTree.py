# This evaluates if both trees have the same structure and values

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        else:
            if p is None or q is None:
                return False
            else:
                if p.val == q.val:
                    left = self.isSameTree(p.left, q.left)
                    right = self.isSameTree(p.right, q.right)
                    return left and right 
                else:
                    return False
