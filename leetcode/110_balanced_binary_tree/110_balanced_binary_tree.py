# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, bal = self.postOrder(root)
        return bal

    def postOrder(self, root):
        if root is None:
            return 0, True

        left_depth, left_bal = self.postOrder(root.left)

        if left_bal:
            right_depth, right_bal = self.postOrder(root.right)
        else:
            return 0, False
        
        return max(left_depth, right_depth) + 1, (right_bal and abs(left_depth - right_depth) <= 1)        