from heapq import *
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks:
            d[task] = 1 + d.get(task, 0)
        
        # Max heap tells us which tasks are ready to be executed.
        # This is giving us the tasks which is ready and has the max frequency.
        max_heap = [-count for count in d.values()]
        heapify(max_heap)

        # Queue
        # Holds the taks being cooldown.
        # Queue will hold (freq, readyTime)
        q = deque()

        time = 0
        while max_heap or q:
            time += 1

            if not max_heap and q:
                time = q[0][1]
            else:
                freq = heappop(max_heap) + 1
                if freq:
                    q.append((freq, time + n))
            if q and q[0][1] == time:
                heappush(max_heap, q.popleft()[0])


            # if q and q[0][1] == time:
            #     heappush(max_heap, q.popleft()[0])

            # if max_heap:
            #     freq = heappop(max_heap) + 1
            #     if freq:
            #         q.append((freq, time + n + 1))

        return time

