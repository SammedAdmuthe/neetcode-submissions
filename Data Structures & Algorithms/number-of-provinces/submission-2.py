
class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]

    def find(self, n):
        while self.par[n] != n:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]

        return n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return True
        
        self.par[p1] = p2
        return False

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        res = n
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    if  not dsu.union(i, j):
                        res-=1
        
        return res
