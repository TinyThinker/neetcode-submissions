class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_time = r

        while l <= r:
            m = l + (r - l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/m)
            
            if total_time <= h:
                min_time = min(min_time, m)
                r = m - 1
            else:
                l = m + 1

        return min_time
        