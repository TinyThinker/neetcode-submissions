class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0

        result = float("inf")
        curr_sum = 0
        for r, num in enumerate(nums):
            print(f"l,r=({l}, {r}), curr_sum={curr_sum}")
            curr_sum += num

            while curr_sum >= target:
                result = min(result, r -l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if result == float("inf") else result

        