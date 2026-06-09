class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i, memo):
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + helper(i - 2, memo), helper(i - 1, memo))

            return memo[i]

        return helper(len(nums) - 1, {})
        