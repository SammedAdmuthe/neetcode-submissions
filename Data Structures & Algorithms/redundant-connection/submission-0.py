
class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]

    def find(self, n):

        while self.par[n] != n:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]

        return n

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return True

        self.par[p1] = p2
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''

            1 -> 2 -> 3 -> 4

            

        '''
        dsu = DSU(len(edges))
        for u, v in edges:
            if dsu.union(u, v):
                return [u, v]
        