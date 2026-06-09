class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or not abbr:
            return False

        w_idx = 0
        a_idx = 0
        while w_idx < len(word) and a_idx < len(abbr):
            if abbr[a_idx].isalpha():
                if abbr[a_idx] == word[w_idx]:
                    w_idx += 1
                    a_idx += 1
                    continue
                else:
                    return False
            else: #is digit per constraits in problem
                if abbr[a_idx] == "0":
                    return False
                
                num = 0
                while a_idx < len(abbr) and abbr[a_idx].isdigit():
                    num = (num * 10) + int(abbr[a_idx])
                    a_idx += 1
                w_idx += num

        return w_idx == len(word) and a_idx == len(abbr)