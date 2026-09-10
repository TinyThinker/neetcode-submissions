class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights + [-1]):
            while stack and heights[stack[-1]] > h:
                selected = stack.pop()
                r = i
                l  = -1
                if stack:
                    l = stack[-1]
                area = (r - l - 1) * heights[selected]
                max_area = max(max_area, area)
            stack.append(i)

        return max_area
        