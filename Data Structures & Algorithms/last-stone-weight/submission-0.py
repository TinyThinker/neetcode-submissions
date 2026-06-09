import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        # Heapify list of stone weights. O(N)
        stones = self.heapify(stones)

        while len(stones) > 1:
            first = self.heapPop(stones)
            second = self.heapPop(stones)

            print(f"first={first}, second={second}")

            if first == second:
                continue

            if first < second:
                self.heapPush(stones, second - first)
            else:
                self.heapPush(stones, first - second)

        return (self.heapPop(stones) if len(stones) == 1 else 0)

    # Helper functions for max heap    
    def heapPush(self, heap: List[int], weight: int):
        heapq.heappush(heap, -weight)

    # Helper functions for max heap
    def heapPop(self, heap: List[int]):
        return -heapq.heappop(heap)

    def heapify(self, stones):
        stones = [-x for x in stones]
        heapq.heapify(stones)
        return stones



