class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                curr_profit = max(prices[sell] - prices[buy], 0)
                max_profit = max(max_profit, curr_profit)
        return max_profit