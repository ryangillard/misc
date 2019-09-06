# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.common_ancestor = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.postOrderReturnOne(root, p, q)

        return self.common_ancestor

    def postOrderReturnOne(self, root, p, q):
        if not root:
            return False

        left = self.postOrderReturnOne(root.left, p, q)
        right = self.postOrderReturnOne(root.right, p, q)

        current_p = root == p
        current_q = root == q

        current = current_p or current_q

        if (left and right) or (left and current) or (current and right):
            self.common_ancestor = root

        return left or current or right

    def postOrderReturnTwo(self, root, p, q):
        if not root:
            return False, False

        l_f_p, l_f_q = self.postOrderReturnTwo(root.left, p, q)
        r_f_p, r_f_q = self.postOrderReturnTwo(root.right, p, q)

        current_p = root == p
        current_q = root == q

        current = current_p or current_q

        left = l_f_p or l_f_q
        right = r_f_p or r_f_q

        if (left and right) or (left and current) or (current and right):
            self.common_ancestor = root

        return left or current, right or current