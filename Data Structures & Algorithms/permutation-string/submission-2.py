class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        # A frequency map of characters in s1
        s1_cnt = {}
        for c in range(ord('a'), ord('z') + 1):
            s1_cnt[chr(c)] = 0
        s2_cnt = s1_cnt.copy()

        for c in s1:
            s1_cnt[c] = 1 + s1_cnt.get(c, 0)


        # Setup a window of size len(s1) and get frequency map of characters in window
        r = 0
        for r in range(len(s1)):
            c = s2[r]
            s2_cnt[c] = 1 + s2_cnt.get(c, 0)

        # Iterate through the windot
        l = 0
        while r < len(s2):
            if s1_cnt == s2_cnt:
                return True

            s2_cnt[s2[l]] -= 1
            l += 1

            r += 1
            if r < len(s2):
                s2_cnt[s2[r]] = 1 + s2_cnt.get(s2[r], 0)


        return False
        