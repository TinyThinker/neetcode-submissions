class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return - 1
        # Binary search. Let's use two pointers starting at opposite sides.
        l, r = 0, len(nums) - 1

        # Let's iterate the loop
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if nums[l] == target:
            return l
        else:
            return -1
