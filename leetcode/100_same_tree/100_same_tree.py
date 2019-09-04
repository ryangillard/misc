# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.iterative(p, q)

    def recursive(self, p, q):
        check = self.nodeCheck(p, q)
        if check == 0:
            return True
        elif check == 1:
            return False

        return self.recursive(p.left, q.left) and self.recursive(p.right, q.right)

    def iterative(self, p, q):
        queue = [(p, q)]

        while queue:
            p, q = queue.pop(0)

            check = self.nodeCheck(p, q)
            if check % 2 == 1:
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True

    def nodeCheck(self, p, q):
        if not p and not q:
            return 0

        if not p or not q:
            return 1

        if p.val != q.val:
            return 1

        return 2