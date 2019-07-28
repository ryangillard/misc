# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        _, _, _, mode = self.findModeRecursive(root)

        return mode
    
    def findModeRecursive(self, root, prev_val=None, cur_count=0, max_count=0, mode=[]):
        if root is None:
            return prev_val, cur_count, max_count, mode

        # Inorder traversal
        prev_val, cur_count, max_count, mode = self.findModeRecursive(root.left, prev_val, cur_count, max_count, mode)
        
        if prev_val is None:
            prev_val = root.val
            cur_count = 1
            max_count = 1
        elif root.val > prev_val:
            prev_val = root.val
            cur_count = 1
        elif root.val == prev_val:
            cur_count += 1

        if cur_count == max_count:
            mode.append(root.val)
        elif cur_count > max_count:
            mode = [root.val]
            max_count = cur_count

        prev_val, cur_count, max_count, mode = self.findModeRecursive(root.right, prev_val, cur_count, max_count, mode)

        return prev_val, cur_count, max_count, mode