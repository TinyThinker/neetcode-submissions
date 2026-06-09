class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s1):
            return False

        freq1 = {}
        for c in s1:
            freq1[c] = 1 + freq1.get(c, 0)

        freq2 = {}
        for i in range(len(s1) - 1):
            freq2[s2[i]] = 1 + freq2.get(s2[i], 0)

        l, r = 0, len(s1) - 1
        while r < len(s2):
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            print(f"freq1 = {freq1}; freq2 = {freq2}")
            if freq1 == freq2:
                return True

            temp_count = freq2.get(s2[l], 1) - 1
            if temp_count > 0:
                freq2[s2[l]] = temp_count
            else:
                del freq2[s2[l]]
            r += 1
            l += 1
        return False


        



