class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = 0
        max_sum = float("-inf")
        for i, num in enumerate(nums):
            if current_sum >= 0:
                current_sum += num
            else:
                current_sum = num

            max_sum = max(max_sum, current_sum)

        return max_sum

        