class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False

        wordDict = set(wordDict)
        return self.bottomUpM2(s, wordDict)

    def bottomUpM3(self, s, wordDict):
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

    def bottomUpM2(self, s, wordDict):
        dp = [True] * (len(s) + 1)
        max_len = max([len(w) for w in wordDict])
        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(max(0, i - max_len), i))

        return dp[-1]