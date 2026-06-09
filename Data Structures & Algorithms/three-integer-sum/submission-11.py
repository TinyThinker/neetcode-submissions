class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            anchor = nums[i]

            # 1. Skip duplicate anchor values
            # This handles the case where the first few elements are duplicates
            if i > 0 and anchor == nums[i-1]:
                continue

            # Optimization: If anchor is positive, and the array is sorted,
            # no three numbers can sum to zero.
            if anchor > 0:
                break

            target = -anchor
            l = i + 1
            r = len(nums) - 1

            while l < r:
                two_sum = nums[l] + nums[r]

                if two_sum == target:
                    result.append([anchor, nums[l], nums[r]])

                    # Move pointers and skip duplicates for both l and r
                    l += 1
                    r -= 1

                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    # Skip duplicates for r
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif two_sum > target:
                    r -= 1
                else: # two_sum < target
                    l += 1
                    
        return result