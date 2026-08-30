class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        """
            r = 0 or c = 0 or r=m or c = n
        """
        seen = set()
        m, n = len(board), len(board[0])
        def markRegion(i, j):
            
            if i < 0 or i>=m or j<0 or j>= n or board[i][j] != "O":
                return 

            board[i][j] = "N"
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                markRegion(i+dr, j+dc)
            return



        for i in range(m):
            if board[i][0] == 'O':
                markRegion(i, 0)
            if board[i][n-1] == 'O':
                markRegion(i, n-1)

        for j in range(n):
            if board[0][j] == 'O':
                markRegion(0, j)
            if board[m-1][j] == 'O':
                markRegion(m-1, j)


        for i in range(m):
            for j in range(n):
                if board[i][j] == "N":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
