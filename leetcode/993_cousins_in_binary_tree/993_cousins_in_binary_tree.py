# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        (x_parent,
         y_parent,
         x_depth,
         y_depth) = self.preorder(root, x, y, 0, -1, -1, -2, -1)

        return self.checkDone(x_parent, y_parent, x_depth, y_depth)

    def preorder(self, root, x, y, depth, x_parent, y_parent, x_depth, y_depth):
        if not root:
            return x_parent, y_parent, x_depth, y_depth

        (x_parent,
         y_parent,
         x_depth,
         y_depth) = self.checkVal(
            root, root.left, x, y, depth, x_parent, y_parent, x_depth, y_depth)

        (x_parent,
         y_parent,
         x_depth,
         y_depth) = self.checkVal(
            root, root.right, x, y, depth, x_parent, y_parent, x_depth, y_depth)

        if self.checkDone(x_parent, y_parent, x_depth, y_depth):
            return x_parent, y_parent, x_depth, y_depth

        (x_parent,
         y_parent,
         x_depth,
         y_depth) = self.preorder(
            root.left, x, y, depth + 1, x_parent, y_parent, x_depth, y_depth)

        if self.checkDone(x_parent, y_parent, x_depth, y_depth):
            return x_parent, y_parent, x_depth, y_depth

        (x_parent,
         y_parent,
         x_depth,
         y_depth) = self.preorder(
            root.right, x, y, depth + 1, x_parent, y_parent, x_depth, y_depth)

        return x_parent, y_parent, x_depth, y_depth

    def checkVal(self, parent, child, x, y, depth, x_parent, y_parent, x_depth, y_depth):
        if child:
            if child.val == x:
                x_parent = parent.val
                x_depth = depth + 1
            elif child.val == y:
                y_parent = parent.val
                y_depth = depth + 1

        return x_parent, y_parent, x_depth, y_depth

    def checkDone(self, x_parent, y_parent, x_depth, y_depth):
        if x_parent == y_parent:
            return False

        if x_depth == y_depth:
            return True

        return False