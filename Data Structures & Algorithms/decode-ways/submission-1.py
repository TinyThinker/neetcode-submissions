class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0 

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            one_back_valid = s[i-1] != "0"
            two_back_valid = 10 <= int(s[i - 2 : i]) <= 26
            print(f"i={i}, one_valid = {one_back_valid}, two_valid = {two_back_valid}")
            dp[i] = one_back_valid * dp[i-1] + two_back_valid * dp[i-2]

        return dp[-1]





        