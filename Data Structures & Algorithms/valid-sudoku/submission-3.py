from collections import defaultdict
class Solution:
    def __init__(self):
        self.rows = defaultdict(list)
        self.cols = defaultdict(list) 
        self.box = defaultdict(list)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We need keep track of all of the elements in each row and make 
        # sure that there are no duplicates. The same process for columns.
        # We can do this process by using a dictionary of each row and what
        # elements are in each. Then we have to do something similar to 
        # the 3x3 boxes. The challenge is how we identify each box. I believe
        # we can do it by identifying it in a tuple (r//3, l//3)

        for row in range(len(board)):
            for col in range(len(board[0])):
                print(f"row={row}, col={col}")
                select = board[row][col]
                if self.valid(select, row, col):
                    if select.isdigit():
                        self.rows[row].append(select)
                        self.cols[col].append(select)
                        self.box[(row//3, col//3)].append(select)
                else:
                    return False

        return True

    def valid(self, select, row, col):
        if select in self.rows[row]:
            print(f"Invalid row. rows[{row}]={self.rows[row]}")
            return False

        if select in self.cols[col]:
            print(f"Invalid col. cols[{col}]={self.cols[col]}")
            return False

        if select in self.box[(row//3, col//3)]:
            print(f"Invalid box. box[({row//3}, {col//3})]={self.box[(row//3, col//3)]}")
            return False

        return True
    
        