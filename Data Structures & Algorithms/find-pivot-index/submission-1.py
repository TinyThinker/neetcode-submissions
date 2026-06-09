class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)

        suffix = []
        total = 0
        for n in reversed(nums):
            total += n
            suffix.append(total)
        suffix.reverse()

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        
        return -1

        