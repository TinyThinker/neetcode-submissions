class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_num = (float("-inf"), None)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            max_num = max(max_num, (count[num], num))
        return max_num[1]