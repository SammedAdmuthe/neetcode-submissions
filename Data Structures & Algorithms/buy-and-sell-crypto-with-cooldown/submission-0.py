class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(indx, is_buy):

            if indx >= len(prices):
                return 0

            if (indx, is_buy) in dp:
                return dp[(indx, is_buy)]
            
            skip = dfs(indx+1, is_buy)
            buy, sell = -math.inf, -math.inf
            if is_buy:
                buy = -prices[indx] +  dfs(indx+1, not is_buy)
            else:
                sell = prices[indx]  + dfs(indx+2, not is_buy)
            
            dp[(indx, is_buy)] = max(skip, buy, sell)
            return dp[(indx, is_buy)]

        return dfs(0, True)