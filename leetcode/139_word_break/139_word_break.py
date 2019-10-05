class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        return self.bottomUp(s, wordDict)

    def bottomUp(self, s, wordDict):
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            if s[i] in wordDict:
                dp[i][i] = True
            else:
                dp[i][i] = False

        i = 0
        j = 0
        for k in range(1, n):
            i = 0
            j = k
            while i < n and j < n:
                if s[i: j + 1] in wordDict:
                    dp[i][j] = True
                else:
                    dp[i][j] = any([dp[i][l] and dp[l + 1][j] for l in range(i, j)])
                i += 1
                j += 1

        return dp[0][-1]