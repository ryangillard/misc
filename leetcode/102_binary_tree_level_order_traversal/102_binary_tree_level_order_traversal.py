# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.levelOrderRecursive(root, 0, [])

    def levelOrderRecursive(self, root, depth, level_order):
        if not root:
            return level_order

        if len(level_order) < depth + 1:
            level_order.append([root.val])
        else:
            level_order[depth].append(root.val)

        level_order = self.levelOrderRecursive(root.left, depth + 1, level_order)

        level_order = self.levelOrderRecursive(root.right, depth + 1, level_order)

        return level_order