class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach  = 0
        
        for i, num in enumerate(nums):
            if max_reach < i:
                return False

            max_reach = max(max_reach, i + nums[i])
        return True