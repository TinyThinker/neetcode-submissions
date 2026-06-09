from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        min_heap = []

        min_heap = [(freq, num) for num, freq in count.items()]
        heapify(min_heap)
        while len(min_heap) > k:
            heappop(min_heap)

        return [num for freq, num in min_heap]

        