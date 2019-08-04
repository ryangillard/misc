# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        
        return self.preOrder(root, root.val)

    def preOrder(self, root, value):
        if not root:
            return True
        
        if root.val != value:
            return False

        if not self.preOrder(root.left, value):
            return False

        return self.preOrder(root.right, value)