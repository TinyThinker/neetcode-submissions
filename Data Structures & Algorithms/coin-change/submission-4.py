class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[-1] == float("inf"):
            return -1 
        return dp[-1]

        # memo = {}

        # def helper(remaining):
        #     if remaining == 0:
        #         return 0
            
        #     if remaining < 0:
        #         return float("inf")

        #     if remaining in memo:
        #         return memo[remaining]

        #     res = float("inf")
        #     for coin in coins:
        #         res = min(res, 1 + helper(remaining - coin))
        #     memo[remaining] = res
        #     return res

        # res = helper(amount)
        # if res == float("inf"):
        #     return -1
        # else:
        #     return res