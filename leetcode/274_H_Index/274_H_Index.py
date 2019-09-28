class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return self.dynamicProgramming(citations)

    def naive(self, citations):
        if not citations:
            return 0

        for h in range(len(citations), 0, -1):
            good_count = 0
            bad_count = 0
            for i in range(len(citations)):
                if citations[i] >= h:
                    good_count += 1
                else:
                    bad_count += 1
                    if bad_count > len(citations) - h:
                        break

            if good_count >= h:
                return h

        return 0
    
    def sort(self, citations):
        citations.sort()

        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i

        return 0

    def dynamicProgramming(self, citations):
        dp = [0] * (len(citations) + 1)

        for i in range(len(citations)):
            if citations[i] > len(citations):
                dp[len(citations)] += 1
            else:
                dp[citations[i]] += 1

        for i in range(len(citations) - 1, -1, -1):
            dp[i] += dp[i + 1]
            if dp[i + 1] >= i + 1:
                return i + 1

        return 0