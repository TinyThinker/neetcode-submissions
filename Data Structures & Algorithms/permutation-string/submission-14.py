class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_size = len(s1)
        if len(s2) < w_size:
            return False

        freq_s1 = {}
        for i in range(w_size):
            freq_s1[s1[i]] = freq_s1.get(s1[i], 0) + 1

        freq_s2 = {}
        for r in range(len(s2)):
            # ingest
            freq_s2[s2[r]] = 1 + freq_s2.get(s2[r], 0)

            # shrink
            if r >= w_size:
                freq_s2[s2[r - w_size]] -= 1
                if not freq_s2[s2[r - w_size]]:
                    del freq_s2[s2[r - w_size]]
            
            # compare
            if r + 1 >= w_size and freq_s2 == freq_s1:
                return True





        return False



