class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:                            # l = 2, r = 5
            m = (r - l) // 2 + l                # m = 3 
            if nums[m] == target:               # 6 == 1 False
                return m

            if nums[m] >= nums[l]:              # is left half sorted
                if nums[l] <= target and nums[m] > target:           # is value in this half
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target and nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            

        return -1
