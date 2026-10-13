class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_size = len(s1)
        if len(s2) < w_size:
            return False

        freq_s1, freq_s2 = {}, {}
        for i in range(w_size):
            freq_s1[s1[i]] = freq_s1.get(s1[i], 0) + 1

        l, r = 0, -1
        while r < len(s2) - 1:
            while r - l + 1 < w_size:
                r += 1
                freq_s2[s2[r]] = freq_s2.get(s2[r], 0) + 1

            if freq_s2 == freq_s1:
                return True

            freq_s2[s2[l]] -= 1
            if not freq_s2[s2[l]]:
                del freq_s2[s2[l]]
            l += 1



        return False

