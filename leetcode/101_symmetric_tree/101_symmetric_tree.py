# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.iterative(root, root)

    def recursive(self, rootf, rootb):
        if not rootf and not rootb:
            return True
        elif not rootf or not rootb:
            return False

        if rootf.val == rootb.val:
            left_right = self.recursive(rootf.left, rootb.right)
            right_left = self.recursive(rootf.right, rootb.left)

            return left_right and right_left

        return False

    def iterative(self, rootf, rootb):
        queue = [rootf, rootb]

        while queue:
            rootf = queue.pop(0)
            rootb = queue.pop(0)

            if not rootf and not rootb:
                # This is ok, but skip this iteration since they won't have vals or children
                continue

            if not rootf or not rootb:
                return False
            elif rootf.val != rootb.val:
                return False

            queue.extend([rootf.left, rootb.right, rootf.right, rootb.left])

        return True