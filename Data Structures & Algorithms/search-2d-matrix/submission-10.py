class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We need to find the row
        l, h = 0, len(matrix) - 1
        row = None
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid][0] > target:
                h = mid - 1
            elif matrix[mid][len(matrix[0]) - 1] < target:
                l = mid + 1
            else:
                row = mid
                break

        if row is None:
            return False

        # Then we do regular binary search.
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r- l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


        