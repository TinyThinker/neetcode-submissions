import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points

        min_heap = []
        for i in range(k):
            x, y = points[i]
            distance = self.get_distance(x, y)
            heapq.heappush(min_heap, (-distance, [x, y]))

        for i in range(k, len(points)):
            min_distance, coordinates = min_heap[0]
            min_distance = -min_distance
            x, y = points[i]
            point_distance = self.get_distance(x,y)
            if point_distance < min_distance:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (-point_distance, [x,y]))

        return [coordinates for distance, coordinates in min_heap]



    def get_distance(self, x, y):
        return math.sqrt(x**2 + y**2)

        