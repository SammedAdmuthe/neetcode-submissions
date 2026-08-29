class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        r, c = len(board), len(board[0])

        def validRows():
            for i in range(r):
                seen = set()
                for j in range(c):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

            return True
    
        def validColumns():
            for i in range(c):
                seen = set()
                for j in range(r):
                    if board[j][i] == ".":
                        continue
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])

            return True

        def validSubBoxes():

            for box in range(9): # 0
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = box//3 * 3 + i
                        col = box%3 * 3 + j
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])

            return True

        return validRows() and validColumns() and validSubBoxes()