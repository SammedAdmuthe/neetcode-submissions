class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def possibleSearch(r, c, indx):
            if indx == len(word):
                return True

            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[indx] or board[r][c] == '#':
                return False

            board[r][c] = '#'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                R, C = r + dr, c + dc
                if possibleSearch(R, C, indx + 1):
                    # board[R][C] = word[indx]
                    return True
            board[r][c] = word[indx]
            return False


        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if possibleSearch(i, j, 0):
                    return True
        
        return False
