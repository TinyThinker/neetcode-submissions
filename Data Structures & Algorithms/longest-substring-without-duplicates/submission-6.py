class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 1
        used = set(s[l])

        maxCount = 1
        while r < len(s):
            if s[r] not in used:
                used.add(s[r])     #("p","w" ) r = 2
                maxCount = max(maxCount, len(used))
                r += 1
            else:
                used.remove(s[l])
                l += 1

        return maxCount
                
            

        
        