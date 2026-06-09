class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        if not word:
            return True

        ROWS = len(board)
        COLS = len(board[0])

        def backtracking(matched, i, j):
            if matched == len(word):
                return True

            if i < 0 or i == ROWS or j < 0 or j == COLS or board[i][j] == "#" or word[matched] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            res = ( backtracking(matched + 1, i+1, j)       or
                    backtracking(matched + 1, i,   j + 1)   or
                    backtracking(matched + 1, i-1, j)       or
                    backtracking(matched + 1, i,   j-1))

            board[i][j] = temp

            return res




        for i in range(ROWS):
            for j in range(COLS):
                if backtracking(0, i, j):
                    return True

        return False

        



        