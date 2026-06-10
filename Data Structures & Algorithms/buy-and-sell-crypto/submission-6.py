class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        if sz <= 1:
            return 0

        l, r = 0, 1
        max_profit = 0
        while r < sz:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if profit < 1:
                l = r
            r += 1

        return max_profit