class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]

        size = len(s)
        if size == 1:
            return True

        l = 0
        r = size - 1

        while l < r:
            if s[l] != s[r]:
                print(f'{s[l]} - {s[r]}')
                return False
            l += 1
            r -= 1

        return True
        