class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_cnt = {}
        for c in s1:
            s1_cnt[c] = 1 + s1_cnt.get(c, 0)

        s2_cnt = {}
        r = 0
        for r in range(len(s1)):
            c = s2[r]
            s2_cnt[c] = 1 + s2_cnt.get(c, 0)

        l = 0
        while r < len(s2):
            if s1_cnt == s2_cnt:
                return True

            s2_cnt[s2[l]] -= 1
            if not s2_cnt[s2[l]]:
                s2_cnt.pop(s2[l])
            l += 1

            r += 1
            if r < len(s2):
                s2_cnt[s2[r]] = 1 + s2_cnt.get(s2[r], 0)


        return False
        