# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = self.preOrder(root, [], set())
        return ["->".join([str(x) for x in path]) for path in paths]

    def preOrder(self, root, path, paths):
        if not root:
            return paths

        if not root.left and not root.right:
            paths.add(tuple(path + [root.val]))

            return paths

        paths = self.preOrder(root.left, path + [root.val], paths)
        paths = self.preOrder(root.right, path + [root.val], paths)

        return paths