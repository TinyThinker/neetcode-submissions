from collections import Counter
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can create a frequency map of the numbers.
        # Then we can insert them into a min heap.
        # Then pop K times.
        # This would give us a time complexity of n if we use heapify.
        # freq = Counter(nums)
        d = defaultdict(int)
        res = []
        for n in nums:
            d[n] += 1

        heap = [(v, k) for k, v in d.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        

        return [x[1] for x in heap]

        