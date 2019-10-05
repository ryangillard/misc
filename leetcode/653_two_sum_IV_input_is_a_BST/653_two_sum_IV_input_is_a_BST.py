# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        hashset = set()
        return self.inorder(root, k, hashset)

    def inorder(self, root, k, hashset):
        if root:
            left = self.inorder(root.left, k, hashset)
            if left or k - root.val in hashset:
                return True
            hashset.add(root.val)
            right = self.inorder(root.right, k, hashset)
            return right

        return False