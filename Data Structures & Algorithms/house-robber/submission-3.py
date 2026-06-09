class Solution:
    def rob(self, nums: List[int]) -> int:
        ledger = [-1] * len(nums)
        for i, amount in enumerate(nums):
            # rob vs no rob
            second_house_amount = 0
            if i - 2 >= 0:
                second_house_amount = ledger[i - 2]    
            rob = nums[i] + second_house_amount

            first_house_amount = 0
            if i - 1 >= 0:
                first_house_amount = ledger[i - 1]
            no_rob = first_house_amount

            ledger[i] = max(rob, no_rob)

        return ledger[-1]
            
                
        