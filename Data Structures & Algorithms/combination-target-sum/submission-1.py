class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx, currState, totalSum):
            if totalSum == target:
                res.append(currState[:])
                return
            
            if totalSum > target or idx >= len(nums):
                return

            # Explore option at idx
            currState.append(nums[idx])
            helper(idx, currState, totalSum + nums[idx])
            currState.pop()

            # Explore option where idx is not included so we explore next idx
            helper(idx + 1, currState, totalSum)                                                                        

        helper(0, [], 0)
        return res