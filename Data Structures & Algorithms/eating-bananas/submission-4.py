import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search_space = [x for x in range(1, max(piles)+1)]
        l, r = 1 , max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            if self.isValid(piles, mid, h):
                r = mid - 1
            else:
                l = mid + 1
        return l
        
    def isValid(self, piles: List[int], k: int, target: int) -> bool:
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        return True if hours <= target else False


