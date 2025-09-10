# Description: Path Sum
# Given the root of a binary tree and an integer targetSum, return 
# true if the tree has a root-to-leaf path such that adding up all 
# the values along the path equals targetSum.

A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def suma(root, curr, target, f):
            if root is None:
                if curr == target and f.left is None and f.right is None:
                    return True
                else:
                    return False
            else:
                if suma(root.left, (curr + root.val), target, root):
                    return True
                else:
                    if suma(root.right, (curr + root.val), target, root):
                        return True
                    else:
                        return False

        if root is None:
            return False
        else:
            return suma(root, 0, targetSum, root)
        
