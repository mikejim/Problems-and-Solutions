# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def maxZZ(node, direction, maxim):
            if not node:
                return maxim

            if direction == "left":
                maxim = max(maxim, maxZZ(node.left, "left", 0), maxZZ(node.right, "right", maxim+1))
            else:
                maxim = max(maxim, maxZZ(node.left, "left", maxim+1), maxZZ(node.right, "right", 0))
            return maxim      

        return max(maxZZ(root.left, "left", 0), maxZZ(root.right, "right", 0)) 
    
