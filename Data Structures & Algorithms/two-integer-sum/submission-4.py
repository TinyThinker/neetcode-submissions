class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can compute what is the number we are looking for and add to a set.
        # For example:
        # i + j = t 
        # if we iterate through the array i values then we know we are looking for 
        # j = t - i. We add it to the set and if we find it we return it.
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            d[target-n] = i
        return None