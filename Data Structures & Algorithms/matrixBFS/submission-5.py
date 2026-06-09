class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        GOAL = (ROWS - 1, COLS - 1)
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Define initial state
        visit = set([(0,0)])
        queue = deque([(0,0)])
        length = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (r,c) == GOAL:
                    return length

                visit.add((r, c))

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue

                    queue.append((nr, nc))
                    # visit.add((nr, nc))
            length += 1

        return - 1
        