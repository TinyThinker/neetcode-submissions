class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCount = 0

        while s:
            start = end = s.pop()
            count = 1
            while (start - 1) in s:
                count += 1
                start = start - 1
                s.remove(start)

            while (end + 1) in s:
                count += 1
                end = end + 1
                s.remove(end)

            maxCount = max (maxCount, count)

        return maxCount
            

        
        