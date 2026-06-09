class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
        search_idx = 0
        for c in t:
            if c == s[search_idx]:
                search_idx += 1

            if search_idx == len(s):
                return True
        return False