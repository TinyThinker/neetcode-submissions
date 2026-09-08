class Solution:
    def trap(self, height: List[int]) -> int:
        # To start this problem we need to understand the invariants.
        # To calculate the water at any point we need to find two things:
        # Is the max value to the left of the current index greater or sm
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        total = 0

        while l < r:
            if height[l] < height[r]:
                total += max_left - height[l]
                l += 1
                max_left = max(max_left, height[l])
            else:
                total += max_right - height[r]
                r -= 1
                max_right = max(max_right, height[r])

        return total

        