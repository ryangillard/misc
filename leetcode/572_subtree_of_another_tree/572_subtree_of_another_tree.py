# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.preorder(s, t)

    def preorder(self, s, t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        valid = self.checkValid(s, t)

        if s.left:
            valid = valid or self.preorder(s.left, t)

        if s.right:
            valid = valid or self.preorder(s.right, t)

        return valid

    def checkValid(self, s, t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        if s.val != t.val:
            return False

        return self.checkValid(s.left, t.left) and self.checkValid(s.right, t.right)