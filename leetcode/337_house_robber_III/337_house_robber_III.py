# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

    def dfs(self, root):
        # Quick exit
        if not root:
            return 0, 0

        # Left subtree
        left_skip_level, left_include_level = self.dfs(root.left)
        
        # Right subtree
        right_skip_level, right_include_level = self.dfs(root.right)
        
        # If we only take the maximums of subtrees by skipping current level
        skip_level = max(left_skip_level, left_include_level) + max(right_skip_level, right_include_level)
        
        # If we include current level and the skip levels below
        include_level = root.val + left_skip_level + right_skip_level

        return skip_level, include_level