# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iterative(root, [])

    def recursive(self, root, inorder_traversal):
        if root:
            inorder_traversal.append(root.val)

            inorder_traversal = self.recursive(root.left, inorder_traversal)

            inorder_traversal = self.recursive(root.right, inorder_traversal)

        return inorder_traversal

    def iterative(self, root, inorder_traversal):
        if root:
            stack = [root]
            while stack:
                root = stack.pop()
                if root:
                    inorder_traversal.append(root.val)
                    stack.extend([root.right, root.left])

        return inorder_traversal