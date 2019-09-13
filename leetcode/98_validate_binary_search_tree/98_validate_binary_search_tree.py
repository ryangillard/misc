# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.preorder(root, -sys.maxint, sys.maxint)

    def preorder(self, root, low, high):
        if not root:
            return True

        # Check root val
        if root.val <= low or root.val >= high:
            return False

        # Check left and right subtree
        if not self.preorder(root.left, low, root.val) or not self.preorder(root.right, root.val, high):
            return False

        # Both left and right subtrees were good
        return True