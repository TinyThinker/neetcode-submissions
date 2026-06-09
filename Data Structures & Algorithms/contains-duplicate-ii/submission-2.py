class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # d = {}
        # for i, num in enumerate(nums):
        #     if num in d and i - d[num] <= k:
        #         return True
        #     d[num] = i


        # return False
        s = set()
        l = 0
        for r, num in enumerate(nums):
            if r - l > k:
                #reduce window
                s.remove(nums[l])
                l += 1
                
            if num in s:
                return True
            s.add(num)

        return False


        