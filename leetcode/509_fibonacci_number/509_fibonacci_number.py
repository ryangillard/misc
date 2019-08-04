class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.dynamicProgramming(N)
    
    def recursive(self, N):
        if N <= 1:
            return N
        else:
            return self.recursive(N - 1) + self.recursive(N - 2)

    def dynamicProgramming(self, N):
        if N <= 1:
            return N

        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(N - 1):
            dp[i + 2] = dp[i + 1] + dp[i]

        return dp[N]

    def formula(self, N):
        return int(round(((1 + 5 ** 0.5) / 2) ** N / 5 ** 0.5))