class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curr_subset, result):
            if i == len(nums):
                result.append(curr_subset[:])
                return

            # Include
            curr_subset.append(nums[i])
            helper(i + 1, nums, curr_subset, result)
            curr_subset.pop()

            # Do not include
            helper(i + 1, nums, curr_subset, result)

        result, curr_subset = [], []
        helper(0, nums, curr_subset, result)
        return result