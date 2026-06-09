class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # A valid window is a window which has already seen all
        # of the characters (with the correct count ) in t
        # In other "words": window[c] >= expected[c]
        # Why greater? we can have  repeated characters. 
        if not t or not s:
            return ""

        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        unique_chars = len(t_count.keys())

        l = 0
        w_count = {}    # current window
        satisfied_chars = 0
        min_window_size = float("infinity")
        min_window_range = (0, 0)
        for r in range(len(s)):
            w_count[s[r]] = 1 + w_count.get(s[r], 0)
            if w_count[s[r]] == t_count.get(s[r], 0):
                satisfied_chars += 1

            while unique_chars == satisfied_chars:
                prev_window_size = min_window_size
                min_window_size = min(min_window_size, r - l + 1)
                if min_window_size != prev_window_size:
                    min_window_range = (l, r)

                w_count[s[l]] -= 1
                if s[l] in t_count and w_count[s[l]] < t_count[s[l]]:
                    satisfied_chars -= 1
                l += 1
            
        
        l, r = min_window_range
        return s[l : r + 1] if min_window_size != float("infinity") else ""
