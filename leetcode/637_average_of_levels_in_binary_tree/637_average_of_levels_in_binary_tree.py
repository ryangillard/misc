# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level_order = self.levelOrderRecursive(root, 0, [])

        level_avg = []
        for level in level_order:
            sum = 0.0
            for val in level:
                sum += val
            level_avg.append(sum / len(level))

        return level_avg

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