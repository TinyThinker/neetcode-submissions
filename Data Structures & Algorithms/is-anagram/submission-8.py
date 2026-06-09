class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        self.populate(char_dict, s)

        for c in t:
            if c in char_dict:
                if char_dict[c] == 1:
                    del char_dict[c]
                else:
                    char_dict[c] -= 1
            else:
                return False
        
        return len(char_dict) == 0


    def populate(self, char_dict: dict, s: str) -> None:
        for c in s:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    