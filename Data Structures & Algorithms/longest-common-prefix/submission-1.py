class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""
        for i, c in enumerate(strs[0]):
            s = set([strs[0][i]])
            for word in strs[1:]:
                if i >= len(word):
                    return result
                s.add(word[i])
                
                if len(s) > 1:
                    return result
            result += s.pop()

        return result
