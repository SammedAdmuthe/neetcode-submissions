from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0

        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh+=1

        time = 0
        while q and fresh:
            
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    R, C = r + dr, c + dc

                    if R < 0 or C < 0 or R >= m or C >= n or grid[R][C] != 1:
                        continue
                    grid[R][C] = 2
                    fresh-=1
                    q.append((R, C))
            
            time+=1


        return time if fresh == 0 else -1



        