class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_substr = 1
        substr_set = set()
        start = 0
        for end in range(len(s)):
            if s[end] not in substr_set:
                substr_set.add(s[end])
                max_substr = max(max_substr, end - start + 1)
            else:
                while s[start] != s[end]:
                    substr_set.remove(s[start])
                    start +=1

                start += 1

        return max_substr



        