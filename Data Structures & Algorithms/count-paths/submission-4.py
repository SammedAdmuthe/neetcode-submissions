class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]

                