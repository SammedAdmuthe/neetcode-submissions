class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])


        max_area = 0
        seen = set()
        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or (i,j) in seen or grid[i][j] == 0:
                return 0

            res = 0
            seen.add((i, j))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                R, C = i + dr, j + dc
                res += 1 + dfs(R, C)

            return res


        for i in range(r):
            for j in range(c):
                if (i, j) not in seen and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area//4