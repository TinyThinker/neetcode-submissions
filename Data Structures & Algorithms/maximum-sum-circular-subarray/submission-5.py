class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum_suffix = [None] * len(nums)
        max_curr_sum, curr_sum = float("-inf"), 0

        for i in range(len(nums) - 1, -1, -1):
            curr_sum += nums[i]
            max_curr_sum = max(curr_sum, max_curr_sum)
            max_sum_suffix[i] = max_curr_sum

        prefix_sum = 0
        max_circular = float('-inf')
        curr_sum = 0
        max_kandane = float('-inf')
        for i, num in enumerate(nums):
            if i + 1 < len(nums):
                prefix_sum += num
                max_circular = max(max_circular, prefix_sum + max_sum_suffix[i + 1])

            curr_sum = max(curr_sum + num, num)
            max_kandane = max(max_kandane, curr_sum)

        return max(max_circular, max_kandane)

        # Input: circular array (int)
        #        Length n
        # Circular properties
        # nums[i] next is nums[(i + 1) % len(nums)]
        # nums[i] previous is nums[(i - 1) % len(nums)]
        # 
        #  Case 1: Sum is no circular (wraps around)
        #  Case 2: Sum is circular

        # OPTIMAL WAY.
        # O(N) Time
        # O(1) Space
        # Total Sum = (prefix sum + suffix sum) + middle_subarray
        # Total_sum = (circular array) + middle_subarray
        # Circular_array = Total_sum - middle_subarray
        # max_circular_array = total_sum - min_subarray
        #
        # min_sum, max_sum = float("inf"), float("-inf")
        # curr_min_sum = curr_max_sum = total_sum = 0

        # for num in nums:
        #     curr_min_sum = min(curr_min_sum + num, num)
        #     min_sum = min(curr_min_sum, min_sum)

        #     curr_max_sum = max(curr_max_sum + num, num)
        #     max_sum = max(curr_max_sum, max_sum)

        #     total_sum += num

        # result = 0
        # if total_sum == min_sum:
        #     result = max_sum
        # else:
        #     result = max(max_sum, total_sum - min_sum)
        # return result









        


        