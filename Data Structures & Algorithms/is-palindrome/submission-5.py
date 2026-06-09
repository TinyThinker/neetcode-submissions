class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse the string and compare it to the nont reversed
        # Since we are only taking alphanumeric characters we need to clean the string
        # from all other characters.
        temp = ""
        for c in s:
            if c.isalnum():
                temp += c.lower()
        return temp == temp[::-1]
            


        # l, r = 0, len(s) - 1
        # s = s.lower()

        # while l < r:
        #     if not s[l].isalnum():
        #         l += 1
        #         print(f"s[l]={s[l] } | is not alphanumeric")
        #         continue
            
        #     if not s[r].isalnum():
        #         print(f"s[r]={s[r] } | is not alphanumeric")
        #         r -= 1
        #         continue

        #     print(f"Comparing s[l]={s[l]}; s[r]={s[r]}")
        #     if s[l] != s[r]:
        #         return False
        #     else:
        #         l += 1
        #         r -= 1

        # return True