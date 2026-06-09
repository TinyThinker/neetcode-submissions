class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        maxSubArray = float("-inf")
        currSum = 0
        for num in nums:
            currSum += num
            maxSubArray = max(maxSubArray, currSum)
            if currSum < 0:
                currSum = 0
        return maxSubArray
        