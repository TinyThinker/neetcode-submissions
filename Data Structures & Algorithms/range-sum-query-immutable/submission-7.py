class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]