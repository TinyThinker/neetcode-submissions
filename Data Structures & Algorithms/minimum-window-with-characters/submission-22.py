class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = None
        if s and t and len(s) < len(t):
            return ""

        T_FREQ = self.createFreq(t)
        NUM_KEYS = len(T_FREQ)

        # Find first solution
        l, r = 0, 0
        s_freq = {}
        have = 0
        min_len = float('inf')
        while r < len(s):
            # Expand to the right until we find a solution
            have += self.addFreq(s_freq, T_FREQ, s[r])
            while have == NUM_KEYS:
                if r - l + 1 < min_len:
                    res = (l, r + 1)
                    min_len = r - l + 1
                have -= self.reduceFreq(s_freq, T_FREQ, s[l])
                l += 1
            r += 1
        return s[res[0]:res[1]] if res else ""

    def reduceFreq(self, d: dict, t: dict, c: str) -> int:
        if c not in d:
            return 0

        d[c] -= 1
        if d[c] == 0:
            del d[c]

        return 1 if c not in d or d[c] < t[c] else 0


    def addFreq(self, d: dict, t: dict, c: str) -> int:
        if c not in t:
            return 0

        d[c] = 1 + d.get(c, 0)
        return d[c] == t[c]

    def createFreq(self, s: str) -> dict:
        d = {}
        for c in s:
            d[c] = 1 + d.get(c, 0)
        return d