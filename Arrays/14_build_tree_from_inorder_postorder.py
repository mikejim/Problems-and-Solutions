# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def TreeInPost(postorder, inorder):
            if not postorder or not inorder:
                return None
            
            lastP = len(postorder)-1
            root_val = postorder[lastP]
            root = TreeNode(root_val)

            mid = inorder.index(root_val)

            root.left = TreeInPost(postorder[:mid], inorder[:mid])
            root.right = TreeInPost(postorder[mid:lastP], inorder[mid+1:])

            return root
        
        return TreeInPost(postorder, inorder)        

