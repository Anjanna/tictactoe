class Game:

    def __init__(self, m, n):
        self.board = [[' ' for _ in range(n)] for _ in range(m)]
        self.currentPlayer = "X"
        self.endGame = False

    def draw_board(self):
        for row in range(len(self.board)):
            if row != 0:
                print("=" * 9)
            for col in range(len(self.board[row])):
                if col != 0:
                    print(" | ", end="")
                print(self.board[row][col], end="")
            print("")

    def _get_player_input(self):
        coordinate = input("Player "+self.currentPlayer+" to choose row and column (0-2): ")
        return [int(_char) for _char in coordinate.replace(" ", "")]

    def _switch_player(self):
        self.currentPlayer = "O" if self.currentPlayer == "X" else "X"

    def _check_row_match(self, row):
        row_match = True
        for i in range(len(self.board[row])):
            if self.board[row][i] != self.currentPlayer:
                row_match = False
                break
        return row_match

    def _check_col_match(self, row, col):
        col_match = True
        for i in range(len(self.board[row])):
            if self.board[i][col] != self.currentPlayer:
                col_match = False
                break
        return col_match

    def _check_diag_match(self, row):
        forward_diag, backward_diag = (True, True)
        for i in range(len(self.board[row])):
            if self.board[i][i] != self.currentPlayer:
                forward_diag = False
            if self.board[i][self.board[row].__len__() - i - 1] != self.currentPlayer:
                backward_diag = False
        return forward_diag or backward_diag

    def did_player_win(self, row, col):
        row_match = self._check_row_match(row)
        col_match = self._check_col_match(row, col)
        diag_match = self._check_diag_match(row)
        return row_match or col_match or diag_match

    def play(self):
        while not self.endGame:
            row, col = self._get_player_input()
            self.board[row][col] = self.currentPlayer
            self.draw_board()
            if self.did_player_win(row, col):
                print(self.currentPlayer+" wins the game!")
                self.endGame = True
            self._switch_player()

    def start_game(self):
        self.draw_board()
        self.play()

game = Game(3, 3)
game.start_game()