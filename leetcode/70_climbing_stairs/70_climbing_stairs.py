class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return self.fib(n)

    def dyn_pro(self, n):
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def fib(self, n):
        ans1 = 0
        ans2 = 1
        for i in range(n):
            ans2, ans1 = ans1 + ans2, ans2
        return ans2