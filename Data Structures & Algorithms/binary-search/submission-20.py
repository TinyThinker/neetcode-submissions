class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            print(f"(l, r, mid) = ({l}, {r}, {mid})")
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
            
        print(f"Exit: (l, r, mid) = ({l}, {r}, {mid})")
        if l < len(nums) and nums[l] == target:
            return l
        else:
            return -1

        [-1, 0, 2, 4, 6, 8]
        mid = 2
        2 < 4

        [4, 6, 8]
        l = 3
        mid = 4
        6 > 4
        r = 4

        [4, 6]
        l = 3
        r = 4
        mid = 3

        # if not nums:
        #     return - 1
        # # Binary search. Let's use two pointers starting at opposite sides.
        # l, r = 0, len(nums) - 1

        # # Let's iterate the loop
        # while l < r:
        #     mid = (r - l) // 2 + l
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1

        # if nums[l] == target:
        #     return l
        # else:
        #     return -1
