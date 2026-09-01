class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPallindrome(i, j):
            # if i < 0:
            #     return [0,r]

            l, r = i, j
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            return [l+1, r-1]
        
        n = len(s)
        count = 0
        ans = ""
        left, right = 0, 0
        for i in range(n):
            
            l, r = isPallindrome(i,i)
            if r-l+1 > right-left+1:
                right, left = r, l

            l, r = isPallindrome(i-1,i)
            if r-l+1 > right-left+1:
                right, left = r, l

        return s[left:right+ 1]


