class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        while num_set: 
            num = num_set.pop()
            count = 1

            next_num = num + 1
            while next_num in num_set:
                count += 1
                num_set.remove(next_num)
                next_num += 1

            prev_num = num - 1
            while prev_num in num_set:
                count += 1
                num_set.remove(prev_num)
                prev_num -= 1
            
            longest = max(longest, count)
        return longest


            
