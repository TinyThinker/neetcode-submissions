class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row via binary search
        top, bottom = 0, len(matrix) - 1
        selected = None
        while top <= bottom:
            m = top + (bottom - top) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                selected = m
                break

        if not top <= bottom:
            return False


        print(f"top={top}, bottom={bottom}")
        #Once we are down to one row
        l, r = 0, len(matrix[selected]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[selected][m] == target:
                return True
            elif matrix[selected][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False