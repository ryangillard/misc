# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_longest = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.postorder(root)

        return self.max_longest

    def postorder(self, root):
        if not root:
            return 0

        left_len = self.postorder(root.left)
        right_len = self.postorder(root.right)

        left = 0
        if root.left and root.left.val == root.val:
            left = left_len + 1

        right = 0
        if root.right and root.right.val == root.val:
            right = right_len + 1

        self.max_longest = max(self.max_longest, left + right)

        return max(left, right)