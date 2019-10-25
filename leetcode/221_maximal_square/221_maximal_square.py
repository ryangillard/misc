class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        return self.dp1D(matrix)

    def dp2D(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        maximum = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
                    maximum = max(maximum, dp[i][j])

        return maximum * maximum

    def dp1D(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        dp = [0] * (n + 1)

        maximum = 0
        previous = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(min(dp[j - 1], previous), dp[j]) + 1
                    maximum = max(maximum, dp[j])
                else:
                    dp[j] = 0

                previous = temp

        return maximum * maximum