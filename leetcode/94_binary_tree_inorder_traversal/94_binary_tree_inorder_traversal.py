# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iterative(root, [])

    def recursive(self, root, inorder_traversal):
        if root:
            inorder_traversal = self.recursive(root.left, inorder_traversal)

            inorder_traversal.append(root.val)

            inorder_traversal = self.recursive(root.right, inorder_traversal)

        return inorder_traversal

    def iterative(self, root, inorder_traversal):
        if root:
            stack = []
            # Add all lefts to the stack
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left

                # Pop lefts off stack
                root = stack.pop()

                # Append to list
                inorder_traversal.append(root.val)

                # Move right from current left and proceed again with pushing lefts due to outer while loop
                root = root.right

        return inorder_traversal