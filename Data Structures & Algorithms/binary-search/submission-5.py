class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, l, r, t):
            if l > r:
                return - 1

            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            if nums[m] < target:
                return binary_search(nums, m + 1, r, target)
            else:
                return binary_search(nums, l, m - 1, target)
        return binary_search(nums, 0, len(nums) - 1, target)
         