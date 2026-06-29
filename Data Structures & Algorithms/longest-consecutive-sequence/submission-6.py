class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        while s:
            longest = max(longest, self.getCurrentLongest(s))

        return longest

    def getCurrentLongest(self, s):
        start = tmp = s.pop()
        count = 1

        while (tmp + 1) in s:
            count += 1
            tmp += 1
            s.remove(tmp)

        tmp = start
        while (tmp - 1) in s:
            count += 1
            tmp -= 1
            s.remove(tmp)


        return count


