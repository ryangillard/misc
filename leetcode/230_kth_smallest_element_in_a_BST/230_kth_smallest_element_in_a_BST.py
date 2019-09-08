# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
        self.answer = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inOrder(root, k)

        return self.answer

    def inOrder(self, root, k):
        if not root:
            return None

        self.inOrder(root.left, k)

        if self.count == 0:
            self.answer = root.val
            self.count += 1
        else:
            if root.val > self.answer and self.count < k:
                self.answer = root.val
                self.count += 1
            else:
                return None

        self.inOrder(root.right, k)

        return None