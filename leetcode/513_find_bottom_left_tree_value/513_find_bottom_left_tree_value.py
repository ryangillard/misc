# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.left_depth = -1
        self.left_value = None

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.preorder(root, 0)

        return self.left_value

    def preorder(self, root, depth):
        if not root:
            return None

        # Since we always go left first, check to see if this is a new deeper depth
        if depth > self.left_depth:
            self.left_depth = depth
            self.left_value = root.val

        # Recurse
        self.preorder(root.left, depth + 1)
        self.preorder(root.right, depth + 1)

        return None