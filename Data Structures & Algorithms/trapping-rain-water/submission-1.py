class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        result = 0
        # We start with pointers to both the beginning and the end
        # Of the array. We will move them towards each other
        # without touching. If they touched that means they are pointing
        # at the same place and there's no water to collect.
        while l < r:
            # What determines if there is water or not?
            # We need to have at least two walls.
            # The smallest wall is the one that determines how much
            # water we can accumulate vertically.
            # Because of this we need a water mark on both sides
            # to see what's the highest point on both sides.
            # From those then we choose the minimum.
            new_height = 0
            if height[l] < height[r]:
                l += 1
                l_max = max(l_max, height[l])
                new_height = height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                new_height = height[r]
            
            min_height = min(l_max, r_max)
            if min_height > new_height:
                result += min_height - new_height


        return result

            




        