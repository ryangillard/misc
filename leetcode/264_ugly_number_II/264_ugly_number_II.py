class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Dynamic programming, keep track of multiples of ugly 2s, 3s, and 5s
        
        # Quick return
        if n <= 0:
            return 0

        # Create dp array
        dp = [1] * n

        # Indices to keep track of last 2, 3, 5 multiple of ugly number
        idx_2 = idx_3 = idx_5 = 0

        # Now loop
        for i in range(1, n):
            dp[i] = min(dp[idx_2] * 2, dp[idx_3] * 3, dp[idx_5] * 5)

            if dp[i] == dp[idx_2] * 2:
                idx_2 += 1

            if dp[i] == dp[idx_3] * 3:
                idx_3 += 1

            if dp[i] == dp[idx_5] * 5:
                idx_5 += 1

        # Return last element in table
        return dp[-1]