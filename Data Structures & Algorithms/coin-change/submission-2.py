class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}
        def possibleWays(amount):

            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            if amount in dp:
                return dp[amount]
            res = math.inf
            for i in range(len(coins)):
                res = min(res, 1 + possibleWays(amount - coins[i]))

            dp[amount] = res
            return res
        
        total_coins = possibleWays(amount)
        return -1 if total_coins == math.inf else total_coins