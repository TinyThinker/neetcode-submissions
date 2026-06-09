class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        if not word:
            return True

        ROWS = len(board)
        COLS = len(board[0])

        def backtracking(current, i, j, visited):
            if i < 0 or i == ROWS or j < 0 or j == COLS or (i,j) in visited or word[len(current)] != board[i][j]:
                return False

            current.append(board[i][j])
            visited.add((i,j))

            if len(current) == len(word):
                return True

            if backtracking(current, i+1, j,     visited):
                return True        # DOWN
            if backtracking(current, i,   j + 1, visited):
                return True           # RIGHT
            if backtracking(current, i-1, j ,    visited):
                return True        # UP
            if backtracking(current, i,   j-1 ,  visited):
                return True        # LEFT

            current.pop()
            visited.remove((i, j))

            return False




        for i in range(ROWS):
            for j in range(COLS):
                if backtracking([], i, j, set()):
                    return True

        return False

        



        