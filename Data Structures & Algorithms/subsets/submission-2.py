class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_state, result = [], []

        def backtrack(idx):
            if idx > len(nums) - 1:
                result.append(curr_state[:])
                return

            # Add number to set
            curr_state.append(nums[idx])
            backtrack(idx + 1)
            curr_state.pop()

            backtrack(idx + 1)

        backtrack(0)
        return result
        