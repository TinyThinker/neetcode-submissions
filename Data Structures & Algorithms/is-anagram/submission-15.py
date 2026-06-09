class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We could sort the strings and make sure that they are the same.
        # This would be an O(n log n) time complexity 
        # While having an O(1) space complexity.
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        # Alterntively we could create a fequency dictionary of characters in both strings.
        # if they are the same then we are good
        # Time complexity O(N)
        # Space complexity O(n)
        d_s, d_t = {}, {}
        for c in s:
            d_s[c] = 1 + d_s.get(c, 0)

        for c in t:
            d_t[c] = 1 + d_t.get(c, 0)

        return d_s == d_t