# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_length = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _ = self.postOrder(root)

        return self.max_length

    def postOrder(self, root):
        if not root:
            return 0

        # left + right is diameter of between left and right subtrees
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)

        self.max_length = max(self.max_length, left + right)

        # Add 1 to max since we're done with this level and can count the node
        return max(left, right) + 1