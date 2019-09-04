class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal_triangle = [None] * 2

        for i in range(rowIndex + 1):
            row = [0] * (i + 1)
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row) - 1):
                row[j] = pascal_triangle[(i - 1) % 2][j - 1] + pascal_triangle[(i - 1) % 2][j]

            pascal_triangle[i % 2] = row

        return pascal_triangle[i % 2]