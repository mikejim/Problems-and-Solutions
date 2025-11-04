# Build a tree using an inorder and preorder list of elements
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        def TreeFromPreIn(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root_val = preorder[0]
            root = TreeNode(root_val)

            mid = inorder.index(root_val)

            root.left = TreeFromPreIn(preorder[1:mid+1], inorder[:mid])
            root.right = TreeFromPreIn(preorder[mid+1:], inorder[mid+1:])

            return root
        
        return TreeFromPreIn(preorder, inorder)
