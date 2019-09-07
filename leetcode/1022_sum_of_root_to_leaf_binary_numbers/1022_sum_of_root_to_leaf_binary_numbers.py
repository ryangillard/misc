# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.inOrder(root, [], 0)

    def inOrder(self, root, path, sum):
        if not root:
            return sum
        
        if not root.left and not root.right:
            # This is a leaf node
            return sum + int("".join(path + [str(root.val)]), 2)

        sum = self.inOrder(root.left, path + [str(root.val)], sum)
        
        sum = self.inOrder(root.right, path + [str(root.val)], sum)
        
        return sum