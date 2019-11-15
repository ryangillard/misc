"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        root = Node(node.val, [])
        stack = [node]
        visited = {}
        visited[node.val] = root

        while stack:
            top = stack.pop()
            
            for neighbor in top.neighbors:
                if neighbor.val not in visited:
                    stack.append(neighbor)
                    visited[neighbor.val] = Node(neighbor.val, [])
                visited[top.val].neighbors.append(visited[neighbor.val])

        return root