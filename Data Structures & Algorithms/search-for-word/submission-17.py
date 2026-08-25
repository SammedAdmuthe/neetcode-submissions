class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def possibleSearch(r, c, indx):
            if indx == len(word):
                return True

            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[indx] or  board[r][c] == '#':
                return False

            board[r][c] = '#'
            res = (possibleSearch(r + 1, c, indx + 1) or
                     possibleSearch(r - 1, c, indx + 1) or
                   possibleSearch(r, c + 1, indx + 1) or
                   possibleSearch(r, c - 1, indx + 1))
            board[r][c] = word[indx]
            return res


        for i in range(n):
            for j in range(m):
                if possibleSearch(i, j, 0):
                    return True
        
        return False
