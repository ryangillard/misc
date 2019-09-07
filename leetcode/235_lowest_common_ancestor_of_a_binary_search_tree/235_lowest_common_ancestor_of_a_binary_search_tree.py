# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.iterative(root, p, q)

    def recursive(self, root, p, q):
        current_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val < current_val and q_val < current_val:
            return self.recursive(root.left, p, q)
        elif p_val > current_val and q_val > current_val:
            return self.recursive(root.right, p, q)

        return root

    def iterative(self, root, p, q):
        p_val = p.val
        q_val = q.val

        while root:
            current_val = root.val
            
            if p_val < current_val and q_val < current_val:
                root = root.left
            elif p_val > current_val and q_val > current_val:
                root = root.right
            else:
                return root

        return None