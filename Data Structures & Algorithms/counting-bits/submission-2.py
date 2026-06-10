class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for x in range(n + 1):
            tmp = x
            cnt = 0
            while tmp:
                cnt += tmp & 1
                tmp >>= 1
            res.append(cnt)

        return res