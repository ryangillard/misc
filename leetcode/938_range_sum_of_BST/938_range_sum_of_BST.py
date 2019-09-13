# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.dfs(root, L, R, 0)

    def dfs(self, root, L, R, range_sum):
        if root:
            if L <= root.val <= R:
                range_sum += root.val

            if L < root.val:
                range_sum = self.dfs(root.left, L, R, range_sum)

            if root.val < R:
                range_sum = self.dfs(root.right, L, R, range_sum)

        return range_sum