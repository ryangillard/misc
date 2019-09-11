# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > key:
            # Go left
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            # Go right
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the key!
            # If there's 0-1 children
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # If there are 2 children, find inorder successor which is the minimum node in the right subtree
            temp = self.inorderSuccessor(root.right, key)

            # Replace root's info with inorder successor's info
            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)

        return root

    def inorderSuccessor(self, root, key):
        # Go as far left as possible
        while root.left:
            root = root.left
        return root