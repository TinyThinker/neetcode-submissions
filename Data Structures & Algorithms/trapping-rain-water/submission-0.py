class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        result = 0

        # find start of left wall
        # we need to make sure that there are two walls 
        # to be able to trap water.
        # the shorter side of the wall determines how much water we can trap

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                result += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                result += rmax - height[r]
        return result




                




        



 

            


        