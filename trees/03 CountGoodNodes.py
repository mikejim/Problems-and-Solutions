# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxN):
            if not root:
                return 0
            total = 0
            if maxN <= root.val:
                total = total + 1
                maxN = root.val
            total = total + dfs(root.left, maxN)
            total = total + dfs(root.right, maxN)            
            return total        
        total = dfs(root, root.val)
        return total
