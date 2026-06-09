class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        if not word:
            return True

        ROWS = len(board)
        COLS = len(board[0])

        def backtracking(matched, i, j, visited):
            if matched == len(word):
                return True

            if i < 0 or i == ROWS or j < 0 or j == COLS or (i,j) in visited or word[matched] != board[i][j]:
                return False

            visited.add((i,j))



            res = (backtracking(matched + 1, i+1, j,     visited) or
                 backtracking(matched + 1, i,   j + 1, visited) or
                 backtracking(matched + 1, i-1, j ,    visited) or
                 backtracking(matched + 1, i,   j-1 ,  visited))

            visited.remove((i, j))

            return res




        for i in range(ROWS):
            for j in range(COLS):
                if backtracking(0, i, j, set()):
                    return True

        return False

        



        