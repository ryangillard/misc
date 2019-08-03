class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        spiral = []
        spiral = self.everySquare(R, C, r0, c0, spiral)
        return spiral

    def everySquare(self, R, C, r0, c0, spiral):
        row = r0
        col = c0
        direction = "right"
        min_row = row
        max_row = row + 1
        min_col = col - 1
        max_col = col + 1

        while True:
            if 0 <= row < R and 0 <= col < C:
                spiral.append([row, col])
                if len(spiral) == R * C:
                    return spiral

            if direction == "right":
                col += 1
                if col == max_col:
                    direction = "down"
                    min_row -= 1
            elif direction == "down":
                row += 1
                if row == max_row:
                    direction = "left"
                    max_col += 1
            elif direction == "left":
                col -= 1
                if col == min_col:
                    direction = "up"
                    max_row += 1
            elif direction == "up":
                row -= 1
                if row == min_row:
                    direction = "right"
                    min_col -= 1