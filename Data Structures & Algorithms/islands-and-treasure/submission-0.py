from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        q = deque()
        for i in range(r):
            for j in range(c):

                if grid[i][j] == 0:
                    q.append((i, j, 0))

        seen = set()
        
        while q:

            row, col, dist = q.popleft()
            if (row, col) in seen:
                continue
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                R, C = row+dr, col+dc

                if R < 0 or R >= r or C < 0 or C >= c or (R, C) in seen or grid[R][C] != 2147483647:
                    continue

                grid[R][C] = dist + 1
                q.append((R, C, dist + 1))