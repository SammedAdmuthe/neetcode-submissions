class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        seen = set()
        m, n = len(heights), len(heights[0])
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]
        def markRegion(i, j, prev, water):
            
            if i < 0 or i>=m or j<0 or j>= n or heights[i][j] < prev or water[i][j]:
                return 

            water[i][j]=1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                markRegion(i+dr, j+dc, heights[i][j], water)
            return


        for i in range(m):
            markRegion(i, 0, -math.inf, pacific)
            markRegion(i, n-1, -math.inf, atlantic)

        for j in range(n):
            markRegion(0, j, -math.inf, pacific)
            markRegion(m-1, j, -math.inf, atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res