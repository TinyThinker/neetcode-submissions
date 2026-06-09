class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_count(s) == self.get_count(t)

    def get_count(self, s):
        d = {}
        for c in s:
            d[c] = 1 + d.get(c, 0)

        return d