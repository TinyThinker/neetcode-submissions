class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Setup initial window
        heap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            if i >= k - 1:
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
            
        return res



        



        