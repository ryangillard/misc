class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        if m == 1:
            return matrix[0]

        n = len(matrix[0])
        if n == 1:
            return [x[0] for x in matrix]

        row = 0
        col = 0
        direction = "right"
        min_row = 0
        max_row = m - 1
        min_col = 0
        max_col = n - 1
        spiral = []
        k = 0

        while k < m * n:
            spiral.append(matrix[row][col])
            if direction == "right":
                col += 1
                if col == max_col:
                    direction = "down"
                    min_row += 1
            elif direction == "down":
                row += 1
                if row == max_row:
                    direction = "left"
                    max_col -= 1
            elif direction == "left":
                col -= 1
                if col == min_col:
                    direction = "up"
                    max_row -= 1
            elif direction == "up":
                row -= 1
                if row == min_row:
                    direction = "right"
                    min_col += 1
            k += 1

        return spiral