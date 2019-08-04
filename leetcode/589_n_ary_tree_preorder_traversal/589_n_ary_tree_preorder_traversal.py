"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.preOrderNAry(root, [])

    def preOrderNAry(self, root, path):
        if not root:
            return path

        path.append(root.val)

        for child in root.children:
            path = self.preOrderNAry(child, path)

        return path