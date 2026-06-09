class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    zeroes.add((i,j))

        for row, column in zeroes:
            # zero the row:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for j in range(len(matrix)):
                matrix[j][column] = 0
        