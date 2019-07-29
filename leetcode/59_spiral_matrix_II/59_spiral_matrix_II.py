class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        row = 0
        col = 0
        direction = "right"
        min_row = 0
        max_row = n - 1
        min_col = 0
        max_col = n - 1
        spiral = [[0 for _ in range(n)] for _ in range(n)]
        k = 0

        while k < n * n:
            spiral[row][col] = k + 1
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