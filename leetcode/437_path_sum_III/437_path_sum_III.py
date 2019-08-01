# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Do preorder traversal
        count = self.preOrder(root, sum, {0: 1}, 0)

        return count

    def preOrder(self, root, sum, hash_map, pre_sum):
        # First check if we are at an actual node
        if not root:
            # Return 0 so we don't affect the count
            return 0

        # Add current node's value to running sum
        pre_sum += root.val

        # Initialize count from history of running sum subtracted by the target sum
        # If it doesn't exist in the dictionary, then initialize to 0
        count = hash_map.setdefault(pre_sum - sum, 0)
        
        # Increment visit count of running sum in dictionary
        # Add running sum to dictionary if not already there
        hash_map[pre_sum] = hash_map.setdefault(pre_sum, 0) + 1

        # Go down the left subtree and increment the count of any solutions below
        count += self.preOrder(root.left, sum, hash_map, pre_sum)
        # Go down the right subtree and increment the count of any solutions below
        count += self.preOrder(root.right, sum, hash_map, pre_sum)

        # We're ready to go back up, so remove a visit count of the running sum from the dictionary
        hash_map[pre_sum] -= 1

        return count
