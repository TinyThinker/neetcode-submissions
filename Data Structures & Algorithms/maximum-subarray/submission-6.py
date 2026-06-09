class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums =      [2, -3, 4, -2, 2, 1, -1, 4]
        # sum =       [2, -1, 3,  1, 3, 4,  3, 7]
        # optimized = [2, -1, 4,  2, 4, 5,  4, 8]
        if len(nums) == 1:
            return nums[-1]

        max_sum, curr_sum = float("-inf"), 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
