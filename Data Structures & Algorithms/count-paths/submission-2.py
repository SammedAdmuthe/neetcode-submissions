class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1
        

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                up = 0
                left = 0
                if i == 0:
                    up = 0
                    left = grid[i][j-1]
                elif j == 0:
                    left = 0
                    up = grid[i-1][j]
                else:
                    up = grid[i-1][j]
                    left = grid[i][j-1]

                grid[i][j] = up + left

        return grid[m-1][n-1]

                