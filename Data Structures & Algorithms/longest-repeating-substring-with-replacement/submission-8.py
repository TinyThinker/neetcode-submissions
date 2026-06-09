class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # This problem can be reduced to expanding a window 
        # to it's maximum size where all of the characters would
        # be the same.
        l = r = longest = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            needed_k = (r - l + 1) - max(count.values())
            if needed_k <= k:
                longest = max(longest, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return longest

        # l0 r4, longest3


