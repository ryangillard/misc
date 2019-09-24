class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = 3
        n = s * s
        
        # Check rows
        for j in range(n):
            check_set = set()
            for i in range(n):
                if board[i][j] != ".":
                    if board[i][j] in check_set:
                        return False
                    else:
                        check_set.add(board[i][j])

        # Check columns
        for i in range(n):
            check_set = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in check_set:
                        return False
                    else:
                        check_set.add(board[i][j])

        # Check blocks
        for k in range(n):
            check_set = set()
            for i in range(s):
                for j in range(s):
                    row = i + (k * s) % n
                    col = j + (k // s) * s
                    if board[row][col] != ".":
                        if board[row][col] in check_set:
                            return False
                        else:
                            check_set.add(board[row][col])

        return True