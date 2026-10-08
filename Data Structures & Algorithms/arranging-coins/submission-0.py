class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''

            1 -> 1
            3 -> 2

            mid (mid + 1)//2 

        '''

        l = 1
        r = n


        while l <= r:
            
            mid = l + (r - l)//2

            sum_of_mid_nums = mid * (mid + 1)//2


            if sum_of_mid_nums <= n:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res