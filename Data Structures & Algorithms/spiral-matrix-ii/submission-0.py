class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
            r1, r2 = 0, row
            c1, c2 = col, 0

            right r1,c2 to r2,c1
            r1+=1
            down r1,c2 to r2, c2

            left row, col to row, 0
            up row, 0 to 0,0
        '''


        r1, c1 = 0, 0
        r2, c2 = n-1, n-1
        grid = [[0 for _ in range(n)] for _ in range(n)]
        
        count = 1
        #move left

        while r1 <= r2 and c1 <= c2:

            for c in range(c1, c2 + 1):
                grid[r1][c] = count
                count+=1

            r1 +=1

            # move down

            for r in range(r1, r2 + 1):
                grid[r][c2] = count
                count +=1

            c2 -=1

            if r1 > r2 and c1 > c2:
                break

            for c in range(c2, c1 - 1, -1):
                grid[r2][c] = count
                count +=1
            r2-=1

            for r in range(r2, r1 - 1, -1):
                grid[r][c1] = count
                count +=1
            c1+=1


        return grid
            