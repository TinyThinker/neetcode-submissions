class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sorted version.
        # This will have a O(n logn) time complexity because of the sorting.
        # This will have O(1) space complexity
        # sz = len(nums)
        # if sz <= 1:
        #     return False

        # nums.sort()
        # i = 1
        # while i < sz:
        #     if nums[i] == nums[i - 1]:
        #         return True
        #     i += 1

        # return False

        # We can use a set. Traverse the list and add to the set. 
        # As we traverse the set we check if the current traversed number is in the set (duplicate)
        s = set()
        for num in nums:
            if num in s:
                return True

            s.add(num)

        return False