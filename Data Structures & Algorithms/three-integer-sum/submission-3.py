class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        anchor = 0
        nums.sort()
        nums_size = len(nums)
        result = set()
        
        print(f"SortedNums = {nums}")

        while anchor < nums_size and nums[anchor] <= 0:
            l = anchor + 1
            r = nums_size - 1
            target = abs(nums[anchor])
            print(f"anchor={anchor}\n l={l}\n r={r} target={target}")

            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    result.add((nums[anchor], nums[l], nums[r]))
                    l += 1
                elif twoSum > target:
                    r -= 1
                else:
                    l += 1
            anchor += 1

        return [list(tup) for tup in result]