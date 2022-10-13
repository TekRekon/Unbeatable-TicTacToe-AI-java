class Board:
    def __init__(self):
        self.board = ['1', '2', '3',
                      '4', '5', '6',
                      '7', '8', '9']

    def print_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n "
              f"{self.board[3]} | {self.board[4]} | {self.board[5]} \n "
              f"{self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def get_board(self):
        return self.board

    def get_cell(self, cell: int):
        return self.board[cell]

    def play_move(self, cell: int, mark):
        self.board[cell] = mark

    def check_win(self):
        if (self.board[0] == self.board[1] == self.board[2] == 'X' or
                self.board[3] == self.board[4] == self.board[5] == 'X' or
                self.board[6] == self.board[7] == self.board[8] == 'X' or
                self.board[0] == self.board[3] == self.board[6] == 'X' or
                self.board[1] == self.board[4] == self.board[7] == 'X' or
                self.board[2] == self.board[5] == self.board[8] == 'X' or
                self.board[0] == self.board[4] == self.board[8] == 'X' or
                self.board[2] == self.board[4] == self.board[6] == 'X'):
            return 'X'
        elif (self.board[0] == self.board[1] == self.board[2] == 'O' or
              self.board[3] == self.board[4] == self.board[5] == 'O' or
              self.board[6] == self.board[7] == self.board[8] == 'O' or
              self.board[0] == self.board[3] == self.board[6] == 'O' or
              self.board[1] == self.board[4] == self.board[7] == 'O' or
              self.board[2] == self.board[5] == self.board[8] == 'O' or
              self.board[0] == self.board[4] == self.board[8] == 'O' or
              self.board[2] == self.board[4] == self.board[6] == 'O'):
            return 'O'
        else:
            if all(cell == 'X' or cell == 'O' for cell in self.board):
                return 'TIE'
            return 'NO_END'
