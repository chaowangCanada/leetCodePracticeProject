class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0

    """
    Player {player} makes a move at ({row}, {col}).
    @param row The row of the board.
    @param col The column of the board.
    @param player The player, can be either 1 or 2.
    @return The current winning condition, can be either:
            0: No one wins.
            1: Player 1 wins.
            2: Player 2 wins.
    """
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1

            if row == col:
                self.diag += 1

            if row + col == self.n - 1:
                self.anti_diag += 1

            if self.row[row] == self.n or self.col[col] == self.n or self.diag == self.n or self.anti_diag == self.n:
                return 1

        if player == 2 :
            self.row[row] -= 1
            self.col[col] -= 1

            if row == col:
                self.diag -= 1

            if row + col == self.n -1:
                self.anti_diag -= 1

            if self.row[row] == -self.n or self.col[col] == -self.n or self.diag == -self.n or self.anti_diag == -self.n:
                return 2
        return 0
