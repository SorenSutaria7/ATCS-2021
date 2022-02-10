import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        for x in range(2):
            self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your pieces - the first to 3 in a row wins!")
        return None

    def print_board(self):
        # TODO: Print the board
        print("  0 1 2")
        print('0', self.board[0][0], self.board[1][0], self.board[2][0])
        print('1', self.board[0][1], self.board[1][1], self.board[2][1])
        print('2', self.board[0][2], self.board[1][2], self.board[2][2])
        return None

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("This spot isn't on the board. Please chose a row and col between 0 and 2")
            return False
        elif self.board[row][col] != "-":
            print("This spot was already filled in")
            return False
        else:
            return True

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return None

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot

        print(player, "'s turn")
        row = int(input("Enter a row: "))
        col = int(input("Enter a column: "))
        while not self.is_valid_move(row, col):
            row = int(input("Enter a row: "))
            col = int(input("Enter a column: "))

        self.place_player(player, row, col)
        return None

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        self.take_manual_turn(player)
        return

    def check_col_win(self, player):
        # TODO: Check col win
        for i in range(len(self.board)):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        for i in range(len(self.board)):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        else:
            return False

    def check_tie(self):
        # TODO: Check tie
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "-":
                    return False
        return True

    def play_game(self):
        # TODO: Play game

        self.print_instructions()
        self.print_board()
        while not (self.check_win("X") or self.check_win("O") or self.check_tie()):
            print("hello")
            self.take_turn("X")
            self.print_board()
            if self.check_win("X"):
                print("Player 1 wins")
            elif self.check_tie():
                print("Tie")
            else:
                self.take_turn("O")
                self.print_board()
                if self.check_win("O"):
                    print("Player 2 wins")
                elif self.check_tie():
                    print("Tie")
        return


