class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.n = n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1

        if row == col:
            self.diag1 += 1 if player == 1 else -1

        if row+col == len(self.row) - 1:
            self.diag2 += 1 if player == 1 else -1

        if self.diag1 == self.n or self.diag2 == self.n or self.row[row] == self.n or self.col[col] == self.n:
            return 1
        elif self.diag1 == -self.n or self.diag2 == -self.n or self.row[row] == -self.n or self.col[col] == -self.n:
            return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
