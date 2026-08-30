class DSU:

    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, node):
        while node != self.par[node]:
            node = self.par[node]

        return node

    def union(self, n1, n2):

        p1 = self.find(n1)
        p2 = self.find(n2)

        self.par[p2] = p1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        components = set()
        for u, v in edges:
            dsu.union(u, v)

        for v in range(n):
            components.add(dsu.find(v))
        
        return len(components)
