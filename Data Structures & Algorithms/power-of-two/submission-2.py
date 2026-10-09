class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        res = 0
        for i in range(32):
            if (n & (1 << i)):
                res+=1

        return res == 1