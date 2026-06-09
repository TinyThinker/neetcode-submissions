class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we will use a two pointer solution
        # the rationale here is that we will adding left pointer and right pointer
        # l + r == target? If so we have found our solution
        # since they are in ascending order we know that
        # if l + r > target we need to add a smaller number to the smallest number [left]
        # this means we need to increase the position of the left pointer to pick the next small number bigger than the current
        # if l + r < target we need to add a bigger number to the highest value

        l = 0
        r = len(numbers) - 1

        while True:
            twoSum = numbers[l] + numbers[r]
            if twoSum == target:
                return [l + 1 , r + 1]

            if twoSum < target:
                l += 1
            else:
                r -= 1

