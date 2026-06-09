class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # I can calculate the prefix sum from left to right
        # and from right to left.
        # l_r = [0, 1, 8, 11, 17, 23]
        # r_l = [  21, 14 ,11 , 6, 0]
        res = -1
        prefix_l = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix_l[i] = prefix_l[i-1] + nums[i-1]

        if prefix_l[-1] == 0:
            res = len(nums) - 1
        prefix_r = 0
        for i in range(len(nums) - 2, -1, -1):
            prefix_r += nums[i+1]
            if prefix_r == prefix_l[i]:
                res = i
            
        return res
        