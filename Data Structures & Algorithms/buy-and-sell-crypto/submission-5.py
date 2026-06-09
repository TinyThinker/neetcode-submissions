class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxProfit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] > 0:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r

        return maxProfit


        