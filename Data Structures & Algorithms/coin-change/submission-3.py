class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float("inf")

            if remaining in memo:
                return memo[remaining]

            res = float("inf")
            for coin in coins:
                res = min(res, 1 + helper(remaining - coin))
                memo[remaining] = res
            return res

        res = helper(amount)
        if res == float("inf"):
            return -1
        else:
            return res