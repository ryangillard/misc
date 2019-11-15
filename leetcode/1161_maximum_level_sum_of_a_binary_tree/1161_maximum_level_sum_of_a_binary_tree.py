# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.level_sums = dict()

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        self.recursive(root, 1)

        max_sum = max([v for v in self.level_sums.values()])
        for i in range(1, len(self.level_sums) + 1):
            if self.level_sums[i] == max_sum:
                return i

    def recursive(self, root, level):
        if root:
            self.level_sums[level] = self.level_sums.setdefault(level, 0) + root.val

            self.recursive(root.left, level + 1)
            self.recursive(root.right, level + 1)

        return