class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
#         min(max(B) - min(B))
#         min(max(B)) = max(A) - K
#         min(-min(B)) = max(min(B)) = min(A) + K

#         max(B) - min(B) = max(A) - K - (min(A) + K) = max(A) - min(A) - 2 * K

        return max(0, max(A) - min(A) - 2 * K)