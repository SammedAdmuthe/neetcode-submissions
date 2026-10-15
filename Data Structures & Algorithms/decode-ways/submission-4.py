class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}
        def decode(i):
            if i >= len(s):
                return 1
            
            if i in dp:
                return dp[i]
            res = 0
            if s[i] != '0':
                res += decode(i+1)

            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and (s[i+1]>='0' and s[i+1] <= '6'))):
                res += decode(i+2)

            dp[i] = res
            return res
        
        return decode(0)