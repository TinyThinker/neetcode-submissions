from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        min_heap = []
        for num, freq in count.items():
            if len(min_heap) == k and freq > min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (freq, num))
            elif len(min_heap) < k:
                heappush(min_heap, (freq, num))



        return [num for freq, num in min_heap]

        