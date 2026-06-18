from collections import Counter
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can create a frequency map of the numbers.
        # Then we can insert them into a min heap.
        # Then pop K times.
        # This would give us a time complexity of n if we use heapify.
        # d = Counter(nums)
        # # d = defaultdict(int)
        # res = []
        # # for n in nums:
        # #     d[n] += 1

        # heap = [(v, k) for k, v in d.items()]
        # heapq.heapify(heap)
        # while len(heap) > k:
        #     heapq.heappop(heap)
        # return [x[1] for x in heap]

        # We can also use bucket sort for a better time complexity 
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        print(f"buckers={buckets}")
        res = []
        for i in range(len(nums), -1, -1):
            print(f"i={i}, buckets[{i}]={buckets[i]}")
            res.extend(buckets[i])
            if len(res) == k:
                break
        return res

        