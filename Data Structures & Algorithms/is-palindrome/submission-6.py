class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We can use a two pointer strategy for this.
        # We'll set a left pointer at 0 and a right pointer at the last position.
        # We will check whether they are the same, if they are not then it's not an palindrome.
        # Then we advance the pointers.
        # When moving the pointers we need to make sure that it's an alpha num
        l, r = 0, len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
            