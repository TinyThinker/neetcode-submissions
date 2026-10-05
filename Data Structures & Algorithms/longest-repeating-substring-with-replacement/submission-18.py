class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        freq = defaultdict(int)
        l, r = 0, 0

        max_len = 0
        max_freq = 0

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while l < r and (r - l + 1 - max_freq) > k:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
            


            



            
        