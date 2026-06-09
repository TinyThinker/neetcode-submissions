class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = min_value = nums[0]

        total_max = nums[0]
        for i in range(1, len(nums)):
            temp_value = max(nums[i], max_value * nums[i], min_value * nums[i])
            min_value = min(nums[i], max_value * nums[i], min_value * nums[i])
            max_value = temp_value
            total_max = max(total_max, max_value)
        
        return total_max

        