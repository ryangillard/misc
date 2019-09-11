class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        transpose = []
        for j in range(n):
            transpose.append([])
            for i in range(m):
                transpose[j].append(A[i][j])

        return transpose