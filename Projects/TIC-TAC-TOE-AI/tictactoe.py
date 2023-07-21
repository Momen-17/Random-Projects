import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


# Create TicTacToe class
class TicTacToe:
    def __init__(self):
        self.current_winner = None # Keep track of winner
        self.board = [' ' for _ in range(9)] # Create 3 by 3 board
    
    # Create print board method
    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # Create print board numbers staticmethod
    @staticmethod
    def print_board_nums():
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # Create available moves method
    def available_squares(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    # Create empty squares method
    def empty_squares(self):
        return ' ' in self.board
    
    # Create number of empty squares method
    def num_empty_squares(self):
        return self.board.count(' ')
    
    # Create make move method
    def make_move(self, square, letter):
        # Assign letter to square
        self.board[square] = letter
        # Check if it was a winner move
        if self.winner(square, letter):
            self.current_winner = letter
    
    # Create winner method
    def winner(self, square, letter):
        # Row win
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True
        
        # Column win
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        # Diagonal win
        if square % 2 == 0:
            # Descending diagonal
            desc_diagonal = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in desc_diagonal):
                return True
            
            # Ascending diagonal
            asc_diagonal = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in asc_diagonal):
                return True
        
        # If all check fail then we don't have a winner yet
        return False



# Create the game play
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    # Initiate a player
    letter = 'X'
    
    # Loop until we have a winner or there is no more empty squares
    while game.empty_squares():
        # Get move from player whose turn it is
        square = x_player.get_move(game) if letter == 'X' else o_player.get_move(game)
        
        # Record move
        game.make_move(square, letter)
        
        # Print the new board state
        if print_game:
            print(f'{letter} makes move to square {square}')
            game.print_board()
            print()
        
        # Check if player won
        if game.current_winner != None:
            if print_game:
                print(f'{letter} won!')
            return letter
        
        # Alternate players
        letter = 'X' if letter == 'O' else 'O'
        
        # Add a little time delay to make things easier to read
        if print_game:
            time.sleep(.8)
    
    # If we break out of the loop then the game is a draw
    if print_game:
        print('It\'s a draw!')


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(50):
        game = TicTacToe()
        x_player = SmartComputerPlayer('X')
        o_player = RandomComputerPlayer('O')
        result = play(game, x_player, o_player, print_game=False)
        
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    
    print(f'X won {x_wins} times, O won {o_wins} times, and {ties} ties.')