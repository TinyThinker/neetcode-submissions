class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 1:
            return 0

        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            result = max(result, self.get_area(l, r, heights))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return result

    def get_area(self, l, r, heights):
        height = min(heights[l], heights[r])
        width = r - l 
        return height * width
            