class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        '''
        1 1 2
        2 1 2
        '''
        coins.sort()

        def possibleWays(indx, amount):

            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if (indx, amount) in dp:
                return dp[(indx, amount)]
            res = 0
            for i in range(indx, len(coins)):
                res = res + possibleWays(i, amount - coins[i])

            dp[(indx, amount)] = res
            return res
        
        total_coins = possibleWays(0, amount)
        return total_coins