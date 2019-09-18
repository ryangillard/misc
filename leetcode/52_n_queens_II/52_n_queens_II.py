class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        column_set = set()
        main_diag_set = set()
        anti_diag_set = set()
        queen_cols = [-1] * n
        solutions = set()

        self.recursive(n, 0, column_set, main_diag_set, anti_diag_set, queen_cols, solutions)

        return len(solutions)

    def recursive(self, n, row, column_set, main_diag_set, anti_diag_set, queen_cols, solutions):
        if row < n:
            for col in range(n):
                if col not in column_set:
                    main_diag_idx = row - col
                    anti_diag_idx = col - (n - 1 - row)
                    if main_diag_idx not in main_diag_set and anti_diag_idx not in anti_diag_set:
                        column_set.add(col)
                        main_diag_set.add(main_diag_idx)
                        anti_diag_set.add(anti_diag_idx)
                        queen_cols[row] = col

                        self.recursive(n, row + 1, column_set, main_diag_set, anti_diag_set, queen_cols, solutions)

                        column_set.remove(col)
                        main_diag_set.remove(main_diag_idx)
                        anti_diag_set.remove(anti_diag_idx)
                        queen_cols[row] = -1
        else:
            board_string = [""] * n
            for row in range(n):
                row_string = ["."] * n
                row_string[queen_cols[row]] = "Q"
                board_string[row] = "".join(row_string)

            solutions.add(tuple(board_string))

        return None