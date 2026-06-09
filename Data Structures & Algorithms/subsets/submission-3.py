class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx, currState):
            if idx >= len(nums):
                res.append(currState[:])
                return

            # Inclusion action
            currState.append(nums[idx])
            helper(idx + 1, currState)
            currState.pop()

            # Exclusion action
            helper(idx + 1, currState)

        helper(0, [])
        return res