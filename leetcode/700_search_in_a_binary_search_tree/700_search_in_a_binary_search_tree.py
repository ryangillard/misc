# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.preorder(root, val)

    def preorder(self, root, val):
        if root:
            if root.val == val:
                return root

            if val < root.val:
                return self.preorder(root.left, val)

            if root.val < val:
                return self.preorder(root.right, val)

        return None