# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the
# nodes you can see ordered from top to bottom.
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        q = deque()
        result = []
        q.append(root)
        while q:
            size = len(q)
            for i in range(0,size):
                ex = q.popleft()
                if ex.left:
                    q.append(ex.left)
                if ex.right:
                    q.append(ex.right)
                if i == size-1:
                    result.append(ex.val)
        return result

        
