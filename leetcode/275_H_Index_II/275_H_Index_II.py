class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(citations)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if citations[mid] == len(citations) - mid:
                return len(citations) - mid

            if citations[mid] <= len(citations) - mid:
                lo = mid + 1
            else:
                hi = mid

        return len(citations) - lo