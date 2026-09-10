class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                selected = stack.pop()
                l, r = -1, i
                if stack:
                    l = stack[-1]
                max_area = max(max_area, (r - l - 1) * heights[selected])

            stack.append(i)

        while stack:
            selected = stack.pop()
            l, r = -1, len(heights)
            if stack:
                l = stack[-1]
            max_area = max(max_area, (r - l - 1) * heights[selected])

        return max_area

        