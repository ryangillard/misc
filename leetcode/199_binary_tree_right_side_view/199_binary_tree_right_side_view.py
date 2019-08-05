# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = self.reverseInOrder(root, 0, {})
        return [view[i] for i in range(len(view))]

    def reverseInOrder(self, root, depth, view):
        if not root:
            return view

        view = self.reverseInOrder(root.right, depth + 1, view)
        if depth not in view:
            view[depth] = root.val
        view = self.reverseInOrder(root.left, depth + 1, view)

        return view