# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.idx = 0

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = self.preOrder(preorder, preorder[0], -sys.maxint, sys.maxint)

        return root

    def preOrder(self, preorder, val, min_val, max_val):
        # Make sure we didn't increment outside of array
        if self.idx >= len(preorder):
            return None

        # Initialize root node in case it ends up connected to a leaf node
        root = None

        # Keeping track of min and max values ensures we don't break rules of BST
        if min_val <= val and val < max_val:
            # Create node
            root = TreeNode(val)
            
            # Increment index for array
            self.idx += 1

            if self.idx < len(preorder):
                # Go left        
                root.left = self.preOrder(preorder, preorder[self.idx], min_val, val)

            if self.idx < len(preorder):                
                # Go right
                root.right = self.preOrder(preorder, preorder[self.idx], val, max_val)

        return root