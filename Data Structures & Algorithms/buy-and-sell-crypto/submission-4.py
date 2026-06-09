class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        max_profit = 0
        for r in range(1, len(prices)):
            local_profit = prices[r] - prices[l]
            max_profit = max(max_profit, local_profit)
            while l < r and prices[l] >= prices[r]:
                l += 1


        return max_profit
        