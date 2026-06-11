class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        signature = 0
        for i in range(len(nums) + 1):
            signature ^= i
        
        for num in nums:
            signature ^= num

        return signature
            
        