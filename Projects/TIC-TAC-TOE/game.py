import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    # Print the state of the board
    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # Print the initialized board numbered 
    @staticmethod
    def print_board_nums():
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # Return the indices of all the available moves in board
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    # Check if game is still running
    def game_running(self):
        return ' ' in self.board # Boolean expression
    
    # Create make move function and check if move is a winning move
    def make_move(self, square, letter):
        if square in self.available_moves():
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # Create winner function to check for a winner
    def winner(self, square, letter):
        # Check winning by row connection
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True
        
        # Check winning by column connection
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        # Check winning by diagonal connection
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True
        
        # If all checks fail that mean we don't have a winner yer or at all
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    # Initialize a player
    letter = 'X'
    
    while game.game_running():
        # Get move from the player whose turn it is
        square = x_player.get_move(game) if letter == 'X' else o_player.get_move(game)
        
        if game.make_move(square, letter):
            # Print which move player played and the new board state
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print()
            
            # If player wins print that they won and return their letter
            if game.current_winner:
                if print_game:
                    print(f'{letter} won!')
                return letter
            
            # Alternate player letter
            letter = 'X' if letter == 'O' else 'O'
            
            # Delay other player move to make it easier to read
            if print_game:
                time.sleep(0.8)
    
    # If the loop is over and no player won then print it's a tie
    if print_game:
        print_game('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player)