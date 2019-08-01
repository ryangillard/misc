# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path = []
        paths = []
        _, paths = self.preOrder(root, sum, path, paths)

        return paths

    def preOrder(self, root, sum, path, paths):
        if root:
            path.append(root.val)
            if not root.right and not root.left:  # make sure we're at a leaf
                if root.val == sum:
                    paths.append(path[:])
                    path.pop()
                    return path, paths
            path, paths = self.preOrder(root.left, sum - root.val, path, paths)
            path, paths = self.preOrder(root.right, sum - root.val, path, paths)
            path.pop()

        return path, paths