class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        GOAL = (ROWS - 1, COLS - 1)
        NEIGHBORS = [(-1, -1), # up, left
                     (-1, 0),  # up
                     (-1, 1),  # up, right
                     (0, -1),  # left
                     (0, 1),   # right
                     (1, -1),  # down, left
                     (1, 0),   # down
                     (1,1)]    # down, right
        
        # Initialize queue
        queue = deque([(0,0)])

        # Initialize visited set
        visited = set([(0,0)])

        # Init length
        length = 0

        while queue:
            length += 1
            for i in range(len(queue)):
                # Are we there yet?
                r, c = queue.popleft()
                if (r,c) == GOAL:
                    return length

                for r_offset, c_offset in NEIGHBORS:
                    n_r, n_c = r + r_offset, c + c_offset
                    if (n_r, n_c) in visited or min(n_r, n_c) < 0 or n_r >= ROWS or n_c >= COLS or grid[n_r][n_c]== 1:
                        continue

                    # If valid exploration
                    queue.append((n_r, n_c))
                    visited.add((n_r, n_c))

        return -1


        