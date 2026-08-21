class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        substr_set = set()

        start = 0
        for end in range(len(s)):
            while s[end] in substr_set:
                substr_set.remove(s[start])
                start += 1
            substr_set.add(s[end])
            max_substr = max(max_substr, len(substr_set))

        
        return max_substr



        