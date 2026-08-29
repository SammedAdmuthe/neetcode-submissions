class Solution:
    def countBits(self, n: int) -> List[int]:
        '''

            0 -> 0 (0)
            1 -> 1 (1)
          010 -> 2 (1)
          011 -> 3 (2)
          100 -> 4 (1)
          101 -> 5 (2)
          110 -> 6 (2)
          111 -> 7 (3)
         1000 -> 8 (1)
        '''
        
        res = [0] * (n+1)
        res[0] = 0
        indx = 1
        for i in range(1, n+1):
            if pow(2, indx+1) == i:
                indx+=1
            res[i] = res[i - pow(2, indx)] + 1
            
        
        return res
