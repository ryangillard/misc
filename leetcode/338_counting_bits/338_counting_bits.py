class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        factor = 1
        switch = 2
        for i in range(1, num + 1):
            if i == switch:
                switch *= 2
                factor *= 2
                dp[i] = 1
            else:
                idx = i - factor
                dp[i] = dp[idx] + 1

        return dp