class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(i, curr, curr_sum):
            if curr_sum == target:
                result.append(curr[:])
                return

            if curr_sum > target:
                return

            if i >= len(nums):
                return

            # Include
            curr.append(nums[i])
            helper(i, curr, curr_sum + nums[i])
            curr.pop()

            # Exclude
            helper(i + 1, curr, curr_sum)



        helper(0, [], 0)
        return result

        