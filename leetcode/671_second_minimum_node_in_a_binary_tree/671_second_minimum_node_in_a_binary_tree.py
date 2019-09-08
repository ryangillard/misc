# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.minimum = None
        self.second_minimum = None

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        self.minimum = root.val

        self.preOrderLookAtRoot(root)

        if self.second_minimum is None:
            return -1

        return self.second_minimum

    def preOrderLookAtChildren(self, root):
        if not root:
            return None

        if root.left:
            if root.right:
                max_child = max(root.left.val, root.right.val)
            else:
                max_child = root.left.val
        else:
            if root.right:
                max_child = root.right.val
            else:
                max_child = self.minimum

        if max_child > self.minimum:
            if self.second_minimum is None:
                self.second_minimum = max_child
            else:
                self.second_minimum = min(self.second_minimum, max_child)

        self.preOrderLookAtChildren(root.left)
        self.preOrderLookAtChildren(root.right)

        return None
    
    def preOrderLookAtRoot(self, root):
        if root:
            if root.val > self.minimum:
                if self.second_minimum is None:
                    self.second_minimum = root.val
                else:
                    self.second_minimum = min(self.second_minimum, root.val)
            elif root.val == self.minimum:
                self.preOrderLookAtRoot(root.left)
                self.preOrderLookAtRoot(root.right)

        return None