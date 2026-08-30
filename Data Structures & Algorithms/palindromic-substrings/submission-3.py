class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def isPallindrome(i, j):
            if i < 0 or i >= n:
                return 0

            l, r = i, j
            count = 0
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    return count

                count+=1
                l-=1
                r+=1
            return count
        
        n = len(s)
        res = 0
        for i in range(n):
            
            res += isPallindrome(i,i)
            res += isPallindrome(i-1,i)

        return res