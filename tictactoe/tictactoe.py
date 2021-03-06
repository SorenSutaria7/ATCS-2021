import random
import time

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        for x in range(2):
            self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    #printing the instructions of the game
    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your pieces - the first to 3 in a row wins!")
        return None

    #printing the tic tac toe board
    def print_board(self):
        # TODO: Print the board
        print("  0 1 2")
        print('0', self.board[0][0], self.board[1][0], self.board[2][0])
        print('1', self.board[0][1], self.board[1][1], self.board[2][1])
        print('2', self.board[0][2], self.board[1][2], self.board[2][2])
        return None

    #determining if a user move is valid
    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        #not possible spot
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("This spot isn't on the board. Please chose a row and col between 0 and 2")
            return False
        #already filled
        elif self.board[row][col] != "-":
            print("This spot was already filled in")
            return False
        else:
            return True

    #placing the player on the board
    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return None

    #allowing user to take a turn until valid
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

    #does a certain type of turn based on current player
    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            depth = 10
            self.take_minimax_turn(player, depth)
        return

    #checks if anyone has won in any of the columns
    def check_col_win(self, player):
        # TODO: Check col win
        for i in range(len(self.board)):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
        return False

    #checks if anyone has won in any of the rows
    def check_row_win(self, player):
        # TODO: Check row win
        for i in range(len(self.board)):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True
        return False

    #checks if anyone has won in any of the diagnools
    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True
        return False

    #checks if anyone has won
    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        else:
            return False

    #checks if there is a tie anywhere
    def check_tie(self):
        # TODO: Check tie
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "-":
                    return False
        return True

    #prints the instructions if it is an npc game
    def print_npc_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("You are player X and the NPC is player O")
        print("Take turns placing your pieces - the first to 3 in a row wins!")
        return None

    #takes a completely random turn
    def take_random_turn(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        while not self.npc_is_valid_turn(row, col):
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        self.place_player('O', row, col)

    #checks that a random turn is valid
    def npc_is_valid_turn(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        elif self.board[row][col] != "-":
            return False
        else:
            return True

    #plays the game with npc style (depends on which version -- random, unbeatable, depth, alpha)
    def play_npc_game(self):
        # TODO: Play game

        self.print_npc_instructions()
        self.print_board()
        while not (self.check_win("X") or self.check_win("O") or self.check_tie()):
            self.take_turn("X")
            self.print_board()
            if self.check_win("X"):
                print("You win!")
            elif self.check_tie():
                print("Tie")
            else:
                self.take_turn("O")
                self.print_board()
                if self.check_win("O"):
                    print("AI wins")
                elif self.check_tie():
                    print("Tie")
        return None

#The original mini max function
    # def mini_max(self, player):
    #     opt_row = -1
    #     opt_col = -1

        #base cases
    #     if(self.check_win('O')):
    #         return (10, None, None)
    #     if(self.check_win('X')):
    #         return (-10, None, None)
    #     if(self.check_tie()):
    #         return (0, None, None)
    #
       #Player O's turn finding best possible turn
    #     if(player == 'O'):
    #         best = -100
    #         for i in range(len(self.board)):
    #             for j in range(len(self.board[i])):
    #                 if self.board[i][j] == '-':
    #                     self.place_player('O', int(i), int(j))
    #                     num = self.mini_max('X')[0]
    #                     self.place_player('-', int(i), int(j))
    #                     if num > best:
    #                         best = num
    #                         opt_row = int(i)
    #                         opt_col = int(j)
    #         return (best, opt_row, opt_col)
        #Player X's Turn finding best possible turn
    #     if (player == 'X'):
    #         worst = 100
    #         for i in range(len(self.board)):
    #             for j in range(len(self.board[i])):
    #                 if self.board[i][j] == "-":
    #                     self.place_player('X', int(i), int(j))
    #                     num = self.mini_max('O')[0]
    #                     self.place_player('-', int(i), int(j))
    #                     if num < worst:
    #                         worst = num
    #                         opt_row = int(i)
    #                         opt_col = int(j)
    #                 return (worst, opt_row, opt_col)

#mini max with depth in it
    def mini_max_depth(self, player, depth):
        opt_row = -1
        opt_col = -1
        #base cases with depth case
        if depth == 0:
            return 0, None, None
        if (self.check_win("O")):
            return (-10, None, None)
        if (self.check_win("X")):
            return (10, None, None)
        if (self.check_tie()):
            return (0, None, None)

        # Player O's Turn finding best possible turn
        if (player == "O"):
            best = -10
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == '-':
                        self.place_player('O', int(i), int(j))
                        num = self.mini_max_depth('X', depth - 1)[0]
                        self.place_player('-', int(i), int(j))
                        if num > best:
                            best = num
                            opt_row = int(i)
                            opt_col = int(j)
            return (best, opt_row, opt_col)

        # Player X's Turn finding best possible turn
        if (player == "X"):
            worst = 10
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == "-":
                        self.place_player('X', int(i), int(j))
                        num = self.mini_max_depth('O', depth - 1)[0]
                        self.place_player('-', int(i), int(j))
                        if num < worst:
                            worst = num
                            opt_row = int(i)
                            opt_col = int(j)
            return (worst, opt_row, opt_col)

 # mini max with alpha beta in it
    def mini_max_alpha_beta(self, player, depth, alpha, beta):
            opt_row = -1
            opt_col = -1
            # base cases with depth case
            if depth == 0:
                return 0, None, None
            if (self.check_win("O")):
                return (-10, None, None)
            if (self.check_win("X")):
                return (10, None, None)
            if (self.check_tie()):
                return (0, None, None)

            # Player O's Turn finding best possible turn
            if (player == "O"):
                best = -10
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if self.board[i][j] == '-':
                            self.place_player('O', int(i), int(j))
                            num = self.mini_max_alpha_beta('X', depth - 1, alpha, beta)[0]
                            self.place_player('-', int(i), int(j))
                            if num > best:
                                best = num
                                opt_row = int(i)
                                opt_col = int(j)
                            alpha = max(alpha, best)
                            if alpha >= beta:
                                break
                return (best, opt_row, opt_col)

            # Player X's Turn finding best possible turn
            if (player == "X"):
                worst = 10
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if self.board[i][j] == "-":
                            self.place_player('X', int(i), int(j))
                            num = self.mini_max_alpha_beta('O', depth - 1, alpha, beta)[0]
                            self.place_player('-', int(i), int(j))
                            if num < worst:
                                worst = num
                                opt_row = int(i)
                                opt_col = int(j)
                            beat = min(beta, worst)
                            if beta <= alpha:
                                break
                return (worst, opt_row, opt_col)

    #calls the current mini max function
    def take_minimax_turn(self, player, depth):
        start = time.time()
        score, row, col = self.mini_max_alpha_beta(player, depth, -100, 100)
        end = time.time()
        print("This turn took:", end - start, "seconds")
        self.place_player(player, row, col)

#playing the actual game until game over
    def play_game(self):
        # TODO: Play game

        self.print_instructions()
        self.print_board()
        while not (self.check_win("X") or self.check_win("O") or self.check_tie()):
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


