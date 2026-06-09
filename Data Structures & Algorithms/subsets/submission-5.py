class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, curr_subset):
            if i == len(nums):
                result.append(curr_subset[:])
                return

            # Include
            curr_subset.append(nums[i])
            helper(i + 1, curr_subset)
            curr_subset.pop()

            # Do not include
            helper(i + 1, curr_subset)


        helper(0, [])
        return result