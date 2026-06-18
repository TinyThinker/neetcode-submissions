class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        l = ""
        res = []
        while i < len(s):
            if s[i] != '#':
                l += s[i]
                i += 1
            else:
                start = i + 1
                end = start + int(l)
                i = end
                res.append(s[start:end])
                l = ""
        return res

            
            
