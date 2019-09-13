# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.preorder(t)

    def preorder(self, t):
        if not t:
            return ""

        # Preorder start of string
        string = str(t.val)

        if t.left:
            # Add left side
            string += "(" + self.tree2str(t.left) + ")"
            if t.right:
                # Add right side
                string += "(" + self.tree2str(t.right) + ")"
        elif t.right:
                # Add empty left, then add right side
                string += "()" + "(" + self.tree2str(t.right) + ")"

        return string