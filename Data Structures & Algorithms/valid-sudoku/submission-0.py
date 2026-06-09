from collections import defaultdict

class Solution:
    def __init__(self):
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.squares = defaultdict(set)

    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(len(board)):
            for j in range(len(board[i])):
                if not self.insert_new_value(i, j, board):
                    return False

        return True

    def insert_new_value(self, i, j, board):
        if board[i][j] == ".":
            return True

        if board[i][j] in self.rows[i]:
            return False
        self.rows[i].add(board[i][j])

        if board[i][j] in self.cols[j]:
            return False
        self.cols[j].add(board[i][j])

        square = (i // 3, j // 3)
        if board[i][j] in self.squares[square]:
            return False
        self.squares[square].add(board[i][j])

        return True

        
        