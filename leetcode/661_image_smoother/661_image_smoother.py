class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        smooth_matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = max(0, i - 1)
                down = min(m - 1, i + 1)
                left = max(0, j - 1)
                right = min(n - 1, j + 1)
                smooth_matrix[i][j] = self.smoother([col[left: right + 1]for col in M[up: down + 1]])

        return smooth_matrix

    def smoother(self, M):
        m = len(M)
        n = len(M[0])
        denominator = m * n
        numerator = 0
        for i in range(m):
            for j in range(n):
                numerator += M[i][j]

        return numerator // denominator