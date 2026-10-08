class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m, n = len(g), len(s)

        i, j = 0, 0
        res = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                i+=1
                j+=1
                res += 1
            else:
                j+=1

        return res