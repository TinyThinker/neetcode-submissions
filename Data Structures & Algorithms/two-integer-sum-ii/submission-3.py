class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while True:
            tmp = numbers[l] + numbers[r]
            if tmp == target:
                break;
            elif tmp > target:
                r -= 1
            else:
                l += 1
                
        return [l + 1, r + 1]
        