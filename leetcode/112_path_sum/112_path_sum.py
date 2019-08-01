# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        found = self.preOrder(root, sum, False)

        return found

    def preOrder(self, root, sum, found):
        if root:
            if not root.right and not root.left:  # make sure we're at a leaf
                if root.val == sum:
                    return True

            found = self.preOrder(root.left, sum - root.val, found)
            if not found:
                found = self.preOrder(root.right, sum - root.val, found)

            return found