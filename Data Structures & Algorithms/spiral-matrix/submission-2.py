class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while l < r and top < bottom:
            # Traverse Top row from left to right
            for i in range(l, r):
                res.append(matrix[top][i])

            # We have traverse the top row so we move the top row to one below 
            top += 1

            # We traverse the right column from top + 1 to the bottom right
            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1

            # This is where it gets tricky.
            if top < bottom:
                for i in range(r - 1, l - 1, -1):
                    res.append(matrix[bottom-1][i])
                bottom -= 1

            if l < r:
                for i in range(bottom - 1, top - 1, -1):
                    res.append(matrix[i][l])
                l +=1

        return res