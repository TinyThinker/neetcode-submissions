class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can compute what is the number we are looking for and add to a set.
        # For example:
        # i + j = t 
        # if we iterate through the array i values then we know we are looking for 
        # j = t - i. We add it to the set and if we find it we return it.
        # This is a time complexity of O(N) as we only need to iterate the 
        # loop once. The space complexity will also be O(N) as we store the missing 
        # element of a pair for each number in the dictionay.
        # d = {}
        # for i, n in enumerate(nums):
        #     if n in d:
        #         return [d[n], i]
        #     d[target-n] = i
        # return None

        # Alternatively we could use a two pointer strategy.
        # For this to work we need to initialize a pointer left at the beginning
        # and a pointer r at the end.
        # Additionally, the numbers need to be sorted so that we can deterministically
        # understand how to move the pointers. 
        # if i + j > t then we move the right pointer to the left as we need to decrease the sum
        # if i + j < t then we move the left pointer to the right as we need to increase the sum.
        # Otherwise it's a match.
        # This is in place so space complexity is O(1) while time complexity is O(n log n)
        nums = [(n, i) for i, n in enumerate(nums)]

        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            two_sum = nums[l][0] + nums[r][0]
            if two_sum == target:
                small = min(nums[l][1], nums[r][1])
                large = max(nums[l][1], nums[r][1])
                return [small, large]
            elif two_sum > target:
                r -= 1
            else:
                l += 1

        return [-1, -1]
                


