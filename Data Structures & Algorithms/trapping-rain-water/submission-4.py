class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = float("-inf"), float("-inf")
        total = 0

        while l < r:
            current = None
            max_left = max(height[l], max_left)
            max_right = max(height[r], max_right)
            if height[l] < height[r]:
                current = l
                l += 1
            else:
                current = r
                r -= 1

            total += self.compute_area(current, max_left, max_right, height)
        return total

    def compute_area(self, current, max_l, max_r, height):
        area = min(max_l, max_r) - height[current]
        if area < 0:
            area = 0
        return area
        