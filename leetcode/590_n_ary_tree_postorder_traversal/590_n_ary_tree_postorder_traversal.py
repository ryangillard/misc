"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.postOrderNAry(root, [])

    def postOrderNAry(self, root, path):
        if not root:
            return path

        for child in root.children:
            path = self.postOrderNAry(child, path)
            
        path.append(root.val)

        return path