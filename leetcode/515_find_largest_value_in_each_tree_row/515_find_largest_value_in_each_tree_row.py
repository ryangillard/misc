# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.preOrder(root, 0, [])

    def preOrder(self, root, depth, max_list):
        if not root:
            return max_list
        
        if depth + 1 > len(max_list):
            max_list.append(root.val)
        else:
            max_list[depth] = max(max_list[depth], root.val)
        
        max_list = self.preOrder(root.left, depth + 1, max_list)
        
        max_list = self.preOrder(root.right, depth + 1, max_list)
        
        return max_list