class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0" or grid[r][c] == "X":
                return 

            grid[r][c] = "X"
            res = (
                        dfs(r+1, c)
                    or   dfs(r, c+1)
                    or   dfs(r-1, c)
                    or   dfs(r, c-1)
                )
            return 
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res

