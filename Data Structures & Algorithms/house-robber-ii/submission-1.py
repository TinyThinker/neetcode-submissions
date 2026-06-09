class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(nums):
            ledger_1 = 0
            ledger_2 = 0

            for i, amount in enumerate(nums):
                rob = ledger_2 + amount
                no_rob = ledger_1

                ledger_1, ledger_2 = max(rob, no_rob), ledger_1

            return max(ledger_1, ledger_2)

        return max(rob_linear(nums[0:-1]), rob_linear(nums[1:]))