class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_l, max_r = 0 , 0
        total = 0

        while l < r:
            if height[l] < height[r]:
                # we know the bottleneck is on the left side and determines
                # how much water is trappet. We also determine that height[r] is the global
                # max.
                max_l = max(max_l, height[l])
                total += max_l - height[l]
                l += 1
            else:
                max_r = max(max_r, height[r])
                total += max_r - height[r]
                r -= 1
        return total

        