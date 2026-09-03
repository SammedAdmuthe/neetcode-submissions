class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = {}
        def countWays(indx):
        
            if indx >= n:
                return 1

            if indx in dp:
                return dp[indx]
            
            res = 0
            if s[indx] != '0':
                res += countWays(indx + 1)
            if indx + 1 < n and ((s[indx] == '2' and s[indx+1] >= '0' and s[indx+1] <= '6') or s[indx] == '1'):
                res += countWays(indx + 2)

            dp[indx] = res
            return res

        return countWays(0)