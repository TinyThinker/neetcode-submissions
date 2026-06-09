class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(remainder):
            if remainder == 0:
                return 0
            elif remainder < 0:
                return float("inf")
            elif remainder in memo:
                return memo[remainder]
            else:
                min_so_far = float("inf")
                for coin in coins:
                    min_so_far = min(1 + helper(remainder - coin), min_so_far)
                memo[remainder] = min_so_far
                return min_so_far

        result = helper(amount) 
        if result < float("inf"):
            return result
        return -1
        