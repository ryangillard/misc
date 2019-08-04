"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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

        for child in root.children:
            level_order = self.levelOrderRecursive(child, depth + 1, level_order)

        return level_order