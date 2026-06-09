class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Constants describing the SHAPE of the matrix
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Supporting data structures.
        q = deque()             # BFS
        visited = set()         # all of the fruit visitted (rotting)
        fresh_fruit = set()     # a set of fresh fruit to know if all rotted or not.
        minutes = -1             # 1 layer of adjacent fruit rots per minute

        # find sources of rot at add them to the queue
        # Also find fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell == 1:
                    fresh_fruit.add((r,c))
                elif cell == 2:
                    q.append((r,c))
                    visited.add((r,c))

        if not fresh_fruit:
            return 0

        while q:
            # Implement logic here
            minutes += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in visited or min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) not in fresh_fruit:
                        continue

                    fresh_fruit.remove((nr, nc))
                    q.append((nr, nc))
                    visited.add((nr, nc))



        if fresh_fruit:
            return -1
        else:
            return minutes

