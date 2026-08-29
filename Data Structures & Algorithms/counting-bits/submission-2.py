class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def getCount(num):
            count = 0
            for i in range(32):
                if 1 << i & num:
                    count+=1
            return count

        res = []
        for i in range(n+1):
            res.append(getCount(i))

        return res