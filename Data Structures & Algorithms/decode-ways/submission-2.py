class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0 

        one_back_ways = 1
        two_back_ways = 1

        for i in range(2, len(s) + 1):
            one_back_valid = s[i-1] != "0"
            two_back_valid = 10 <= int(s[i - 2 : i]) <= 26
            one_back_ways, two_back_ways = one_back_valid * one_back_ways + two_back_valid * two_back_ways, one_back_ways

        return one_back_ways





        