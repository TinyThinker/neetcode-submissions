class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and self.dfs(r, c, visited, grid, ROWS, COLS):
                    islands += 1

        return islands

    def dfs(self, r: int, c: int, visited: set, grid, ROWS, COLS):
        if min(r, c) == -1 or (r, c) in visited or r == ROWS or c == COLS or grid[r][c] == "0":
            return False

        visited.add((r,c))

        self.dfs(r - 1, c, visited, grid, ROWS, COLS)
        self.dfs(r + 1, c, visited, grid, ROWS, COLS)
        self.dfs(r, c - 1, visited, grid, ROWS, COLS)
        self.dfs(r, c + 1, visited, grid, ROWS, COLS)

        return True