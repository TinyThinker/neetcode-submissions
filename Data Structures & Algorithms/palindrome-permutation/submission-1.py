class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        keys = list(count.keys())
        for k in keys:
            if count[k] % 2 == 0:
                del count[k]
            else:
                count[k] = 1

        return len(count) == 1 or len(count) == 0

        