class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0

        res_len, res_idx = 0, 0
        for i in range(len(s)):
            size, idx = test_palindrome(s, i)
            if size > res_len:
                res_len, res_idx = size, idx
        return s[res_idx : res_idx + res_len]

            
def test_palindrome(s, i):
    size, idx = helper(s, i, True)
    size2, idx2 = helper(s, i, False)

    if size > size2:
        return size, idx
    else:
        return size2, idx2

    
def helper(s, i, even):
    if even:
        l, r = i, i + 1
    else:
        l, r = i, i

    res_len = 0
    res_idx = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r - l + 1) > res_len:
            res_len = r - l + 1
            res_idx = l
        l -= 1
        r += 1

    return res_len, res_idx



        