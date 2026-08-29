class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(0, price - min_buy, max_profit)

        return max_profit