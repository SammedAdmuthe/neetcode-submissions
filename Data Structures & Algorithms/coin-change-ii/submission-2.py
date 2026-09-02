class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        '''
        1 1 2
        2 1 2
        '''
        coins.sort()

        def possibleWays(indx, amount):
            
            if indx == len(coins) and amount == 0:
                return 1
            if amount < 0 or indx == len(coins):
                return 0

            if (indx, amount) in dp:
                return dp[(indx, amount)]

            dp[(indx, amount)] = (
                    possibleWays(indx, amount - coins[indx])  # Use it
                    + possibleWays(indx + 1, amount)          # Skip it
                )

           
            return dp[(indx, amount)]
        
        total_coins = possibleWays(0, amount)
        return total_coins