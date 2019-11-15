# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.iterative(root, 0)

        return root

    def recursive(self, root, cum_sum):
        if not root:
            return cum_sum

        cum_sum = self.recursive(root.right, cum_sum)
        temp = root.val
        root.val += cum_sum
        cum_sum += temp
        cum_sum = self.recursive(root.left, cum_sum)

        return cum_sum

    def iterative(self, root, cum_sum):
        if root:
            stack = []
            # Add all rights to the stack
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.right

                # Pop rights off stack
                root = stack.pop()

                # Update root.val and cum_sum
                temp = root.val
                root.val += cum_sum
                cum_sum += temp

                # Move left from current right and proceed again with pushing rights due to outer while loop
                root = root.left

        return None