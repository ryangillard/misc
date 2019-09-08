# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iterative(root, [])

    def recursive(self, root, inorder_traversal):
        if root:
            inorder_traversal = self.recursive(root.left, inorder_traversal)

            inorder_traversal = self.recursive(root.right, inorder_traversal)

            inorder_traversal.append(root.val)

        return inorder_traversal

    def iterative(self, root, inorder_traversal):
        if root:
            stack = [(root, False)]
            while stack:
                root, visited = stack.pop()
                if root:
                    if visited:
                        # From bubbling back up from our stack
                        # Leaves get a True when we also appended their None left and right
                        inorder_traversal.append(root.val)
                    else:
                        # Since these will be popped in reverse order
                        # We first want to visit left, then right, then root
                        stack.extend([(root, True), (root.right, False), (root.left, False)])

        return inorder_traversal