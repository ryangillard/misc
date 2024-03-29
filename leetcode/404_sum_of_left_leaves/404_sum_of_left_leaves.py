# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.inOrder(root)

        return self.sum

    def inOrder(self, root):
        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val
        
        self.inOrder(root.left)
        self.inOrder(root.right)

        return