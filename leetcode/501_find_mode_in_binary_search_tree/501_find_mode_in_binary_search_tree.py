# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.prev_val = None
        self.cur_count = 0
        self.max_count = 0
        self.mode = []

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Exit early
        if not root:
            return []

        # Whether we want to use global or local version
        use_globals = True
        if use_globals:
            self.findModeRecursiveGlobals(root)
        
            return self.mode
        else:
            _, _, _, mode = self.findModeRecursiveLocals(root)

            return mode

    def findModeRecursiveLocals(self, root, prev_val=None, cur_count=0, max_count=0, mode=[]):
        if root is None:
            return prev_val, cur_count, max_count, mode

        # Inorder traversal
        prev_val, cur_count, max_count, mode = self.findModeRecursiveLocals(root.left, prev_val, cur_count, max_count, mode)

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

        prev_val, cur_count, max_count, mode = self.findModeRecursiveLocals(root.right, prev_val, cur_count, max_count, mode)

        return prev_val, cur_count, max_count, mode
    
    def findModeRecursiveGlobals(self, root):
        if root is None:
            return None

        # Inorder traversal
        self.findModeRecursiveGlobals(root.left)
        
        if self.prev_val is None:
            self.prev_val = root.val
            self.cur_count = 1
            self.max_count = 1
        elif root.val > self.prev_val:
            self.prev_val = root.val
            self.cur_count = 1
        elif root.val == self.prev_val:
            self.cur_count += 1

        if self.cur_count == self.max_count:
            self.mode.append(root.val)
        elif self.cur_count > self.max_count:
            self.mode = [root.val]
            self.max_count = self.cur_count
            
        self.findModeRecursiveGlobals(root.right)

        return None