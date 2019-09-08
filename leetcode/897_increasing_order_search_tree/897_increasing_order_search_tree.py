# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder_traversal = self.inOrder(root, [])

        tail = TreeNode(inorder_traversal[-1])

        for val in inorder_traversal[:-1][::-1]:
            node = TreeNode(val)
            node.right = tail
            tail = node

        return tail

    def inOrder(self, root, inorder_traversal):
        if root:
            inorder_traversal = self.inOrder(root.left, inorder_traversal)
            inorder_traversal.append(root.val)
            inorder_traversal = self.inOrder(root.right, inorder_traversal)

        return inorder_traversal