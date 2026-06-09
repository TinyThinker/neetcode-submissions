class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can use a dictionary (hash map)
        nums_d = {}

        for i, num in enumerate(nums):
            x = target - num
            if x in nums_d:
                return [nums_d[x], i]
            nums_d[num] = i



        