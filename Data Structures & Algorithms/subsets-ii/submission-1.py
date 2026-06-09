class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        def helper(i, curr_subset):
            if i == len(nums):
                result.append(curr_subset[:])
                return
            
            # Include
            curr_subset.append(nums[i])
            helper(i + 1, curr_subset)
            curr_subset.pop()

            # Not Include
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i + 1, curr_subset)

            

        helper(0, [])
        return result
        