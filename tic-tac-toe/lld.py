# Tic Tac Toe Game Implementation


#3x3 board
#X's and O's

#winning condition
#1. Three in a row horizontally
#2. Three in a row vertically
#3. Three in a row diagonally

#Game ending conditions:
#1. Board filled

#check for invalid moves


# entities
# GameBoard
# Player



# design challenges
# 1. player - hhuman/Ai -- factory and strategy pattern
# send notifications - Observer pattern
# game playing -- strategy 
# game state - state pattern pX->pO -> poWin -> pxwin

from abc import ABC, abstractmethod

class HumanPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
class PlayerFactory:
    def create_player(player_type, name, symbol):
        if player_type == "human":
            return HumanPlayer(name, symbol)
        elif player_type == "ai":
            return "AI Player"
        else:
            raise ValueError("Unknown player type")
        
class PlayerStrategy(ABC):
    @abstractmethod
    def make_move(self, board):
        pass

class HumanPlayerStrategy(PlayerStrategy):

    def __init__(self, player):
        self.player_name = player.name

    def make_move(self):
        print(f"{self.player_name}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        return row, col

class GameBoard:

    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.moves_count = 0

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def make_move(self, row, col, player_symbol):
        self.board[row][col] = player_symbol
        self.moves_count += 1

    def is_full(self):
        return self.moves_count == 9

    def check_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' '
    
    def check_winner(self):
        # Check rows
        for row in range(self.size):
            if self.board[row][0] != ' ' and all(self.board[row][col] == self.board[row][0] for col in range(self.size)):
                return True

        # Check columns
        for col in range(self.size):
            if self.board[0][col] != ' ' and all(self.board[row][col] == self.board[0][col] for row in range(self.size)):
                return True

        # Check main diagonal
        if self.board[0][0] != ' ' and all(self.board[i][i] == self.board[0][0] for i in range(self.size)):
            return True

        # Check anti-diagonal
        if self.board[0][self.size - 1] != ' ' and all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] for i in range(self.size)):
            return True

        return False
    

class Games:
    def play():
        pass


class TicTacToeGame(Games):
    def __init__(self):
        self.board = GameBoard()
        self.player1 = PlayerFactory.create_player("human", "Player 1", "X")
        self.player2 = PlayerFactory.create_player("human", "Player 2", "O")
        self.current_player = self.player1

    def play(self):
        
        while True:
            self.board.display()
            row, col = HumanPlayerStrategy(current_player).make_move()
            
            if not self.board.check_valid_move(row, col):
                print("Invalid move. Try again.")
                continue
            
            self.board.make_move(row, col, current_player.symbol)
            
            # Check for win or draw conditions here (not implemented)
            if self.board.check_winner():
                self.board.display()
                print(f"{current_player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            
            # Switch players
            current_player = self.player2 if current_player == self.player1 else self.player1
        




        


        
    