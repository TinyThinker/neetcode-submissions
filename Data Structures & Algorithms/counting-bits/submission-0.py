class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            counter = 0
            n = i
            while n:
                if 1 & n:
                    counter += 1
                n >>= 1
            res.append(counter)
        return res
        