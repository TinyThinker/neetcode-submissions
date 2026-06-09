class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Input: circular array (int)
        #        Length n
        # Circular properties
        # nums[i] next is nums[(i + 1) % len(nums)]
        # nums[i] previous is nums[(i - 1) % len(nums)]
        # 
        #  Case 1: Sum is no circular (wraps around)
        #  Case 2: Sum is circular

        min_sum, max_sum = float("inf"), float("-inf")
        curr_min_sum = curr_max_sum = total_sum = 0

        for num in nums:
            curr_min_sum = min(curr_min_sum + num, num)
            min_sum = min(curr_min_sum, min_sum)

            curr_max_sum = max(curr_max_sum + num, num)
            max_sum = max(curr_max_sum, max_sum)

            total_sum += num

        result = 0
        if total_sum == min_sum:
            result = max_sum
        else:
            result = max(max_sum, total_sum - min_sum)
        return result

        


        