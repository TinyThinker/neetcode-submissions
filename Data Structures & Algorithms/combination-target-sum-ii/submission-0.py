class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(currentState, totalSum, idx):
            if totalSum == target:
                res.append(currentState[:])
                return
            
            if totalSum > target or idx >= len(candidates):
                return

            # Include number at index
            currentState.append(candidates[idx])
            helper(currentState, totalSum + candidates[idx], idx + 1)
            currentState.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            helper(currentState, totalSum, idx + 1)
                
        helper([], 0, 0)
        return res