"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.dfs(root)

    def dfs(self, root):
        if root:
            if root.children:
                return self.inOrder(root, 0, 0) + 2
            else:
                return self.inOrder(root, 0, 0) + 1
        else:
            return 0

    def inOrder(self, root, current_depth, max_depth):
        if not root:
            return max_depth

        for child in root.children:
            max_depth = self.inOrder(child, current_depth + 1, max_depth)
            if current_depth > max_depth:
                max_depth = current_depth

        return max_depth