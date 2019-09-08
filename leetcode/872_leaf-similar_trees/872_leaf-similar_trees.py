# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = self.preOrder(root1, [])
        seq2 = self.preOrder(root2, [])

        if len(seq1) != len(seq2):
            return False

        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                return False

        return True

    def preOrder(self, root, seq):
        if root:
            if not root.left and not root.right:
                seq.append(root.val)
                return seq

            seq = self.preOrder(root.left, seq)
            seq = self.preOrder(root.right, seq)

        return seq