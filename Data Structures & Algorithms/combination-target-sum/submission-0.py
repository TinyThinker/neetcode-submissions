class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currState, res = [], []

        def backtracking(idx, total):
            if total == target:
                res.append(currState[:])
                return

            if total > target or idx > len(nums) - 1:
                return

            currState.append(nums[idx])
            backtracking(idx, total + nums[idx])
            currState.pop()

            backtracking(idx + 1, total)




            

        backtracking(0, 0)
        return res