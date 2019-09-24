class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        row_lists = [""] * numRows
        current_row = 0
        direction = 1
        for i in range(len(s)):
            row_lists[current_row] = row_lists[current_row] + s[i]
            if direction == 0:  # up
                current_row -= 1
                if current_row == 0:
                    direction = 1
            else:  # down
                current_row += 1
                if current_row == numRows - 1:
                    direction = 0

        return "".join(row_lists)