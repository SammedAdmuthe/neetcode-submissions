class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = {}
        def lcs(i, j):

            if i == m or j == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            res = 0
            if text1[i] == text2[j]:
                return 1 + lcs(i+1, j+1)

            res = max(lcs(i+1, j), lcs(i, j+1), lcs(i+1, j+1))
            
            dp[(i,j)] = res
            return res
        
        return lcs(0, 0)