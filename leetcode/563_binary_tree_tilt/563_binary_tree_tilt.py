# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total_tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.postorder(root, 0)

        return self.total_tilt

    def postorder(self, root, total_tilt):
        if not root:
            return 0

        left_sum = self.postorder(root.left, total_tilt)
        right_sum = self.postorder(root.right, total_tilt)

        self.total_tilt += abs(left_sum - right_sum)

        total_sum = left_sum + right_sum + root.val

        return total_sum