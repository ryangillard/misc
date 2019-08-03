# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Return if there is no tree
        if not root:
            return None

        # Create new tree node to act as the "new" root
        tree = TreeNode(root.val)

        # If root is leaf, return tree node
        if not root.right and not root.left:
            return tree

        # Switch left subtree to be new right subtree
        tree.right = self.invertTree(root.left)

        # Switch right subtree to be new left subtree
        tree.left = self.invertTree(root.right)

        return tree