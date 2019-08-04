class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        # Quick return if only one node
        if label == 1:
            return [1]

        # Calculate for binary tree without zigzag
        binary = bin(label)[2:]
        ans = [int(binary[:-i], 2) for i in range(1, len(binary))]
        ans = ans[::-1] + [label]
        
        # Adjust values based on level of tree
        for i in range(len(ans) - 2, 0, -2):
            ans[i] = 2**(i + 1) - 1 + 2**i - ans[i]

        return ans