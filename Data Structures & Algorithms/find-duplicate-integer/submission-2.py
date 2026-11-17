class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast and slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        print(f"slow={slow}, fast={fast}")
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

