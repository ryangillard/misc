class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_triangle = []

        for i in range(numRows):
            row = [0] * (i + 1)
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row) - 1):
                row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

            pascal_triangle.append(row)

        return pascal_triangle