class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(i):
            if i >= len(nums):
                return 0

            no_rob_amount = 0
            if i + 1 in memo:
                no_rob_amount = memo[i + 1]
            else:
                no_rob_amount = helper(i + 1)
                memo[i + 1] = no_rob_amount

            rob_amount = nums[i]
            if i + 2 in memo:
                rob_amount += memo[i + 2]
            else:
                rob_amount += helper(i + 2)
                memo[i + 2] = rob_amount

            return max(no_rob_amount, rob_amount)

        return helper(0)
        