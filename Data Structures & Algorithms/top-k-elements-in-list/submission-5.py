class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = [(freq * -1, num) for num, freq in count.items()]
        heapq.heapify(heap)
        print(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
