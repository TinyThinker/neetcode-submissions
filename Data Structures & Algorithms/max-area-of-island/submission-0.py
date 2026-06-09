class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            # Base case
            if (r,c) in visited or r >= ROWS or c >= COLS or min(r,c) < 0 or grid[r][c] == 0 :
                return 0

            # Recursive case
            visited.add((r,c))
            count = 1
            count += dfs(r - 1, c)
            count += dfs(r + 1, c)
            count += dfs(r, c - 1)
            count += dfs(r, c + 1)

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)

        return max_area

