# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Return early if there is no tree
        if not root:
            return 0

        # Add root to top of stack
        stack = [root]
        # Initialize min depth to 1 because of root
        min_depth = 1
        # Loop until the stack is empty for BFS
        while stack:
            # Store stack size coming into current depth
            stack_size = len(stack)

            # Iterate through stack
            for i in range(stack_size):
                # Return if leaf node since this would be the very first leaf!
                if not stack[i].left and not stack[i].right:
                    return min_depth

                # Add left node to stack
                if stack[i].left:
                    stack.append(stack[i].left)

                # Add right node to stack
                if stack[i].right:
                    stack.append(stack[i].right)

            # Remove prior depth's nodes from stack
            stack = stack[stack_size:]

            # Increment depth as we go down a level in BFS
            min_depth += 1