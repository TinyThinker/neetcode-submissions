class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        GOAL = (ROWS - 1, COLS - 1)

        def dfs(r, c, visit):
            # Base case for failure
            # If out of bounds, if visited or if rocks have been found
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 1:
                return 0

            # Base Case for success
            # If we have reached the goal
            if (r,c) == GOAL:
                print(f"GOAL. ({r}, {c})")
                return 1

            # Recursive case
            count = 0
            visit.add((r,c))
            count += dfs(r + 1, c, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c - 1, visit)
            count += dfs(r, c + 1, visit)

            visit.remove((r,c))

            return count

        return dfs(0, 0, set())
