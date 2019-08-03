# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)

    def bfs(self, root):
        # Return early if there is no tree
        if not root:
            return 0

        # Add root to top of stack
        stack = [root]
        # Initialize min depth to 1 because of root
        max_depth = 1
        # Loop until the stack is empty for BFS
        while stack:
            # Store stack size coming into current depth
            stack_size = len(stack)

            # Iterate through stack
            for i in range(stack_size):
                # Add left node to stack
                if stack[i].left:
                    stack.append(stack[i].left)

                # Add right node to stack
                if stack[i].right:
                    stack.append(stack[i].right)

            # Remove prior depth's nodes from stack
            stack = stack[stack_size:]

            # Increment depth as we go down a level in BFS
            max_depth += 1

        return max_depth - 1

    def dfs(self, root):
        return self.inOrder(root, 0, 0) + 1 if root else 0

    def inOrder(self, root, current_depth, max_depth):
        if not root:
            return max_depth

        max_depth = self.inOrder(root.left, current_depth + 1, max_depth)
        if current_depth > max_depth:
            max_depth = current_depth
        max_depth = self.inOrder(root.right, current_depth + 1, max_depth)

        return max_depth