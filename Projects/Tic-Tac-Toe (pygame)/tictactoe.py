import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.player = 'X'
        self.num_of_plays = 0
        self.current_winner = None
        self.board = [' ' for _ in range(9)]
    
    # Print the current board state
    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # Print the numbered board as initialization
    @staticmethod
    def print_board_nums():
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # The indices of all available squares
    def available_squares(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    # Check if game is still running
    def still_running(self):
        return ' ' in self.board # Boolean expression
    
    # Create make move function
    def make_move(self, square, letter):
        # Assign the letter to the square
        self.board[square] = letter
        # Check if it was a winning move
        if self.winner(square, letter):
            self.current_winner = letter
    
    # Create check win function
    def winner(self, square, letter):
        if self.num_of_plays >= 5:
            # Row win
            row_ind = square // 3
            row = self.board[row_ind * 3: (row_ind + 1) * 3]
            if all(spot == letter for spot in row):
                return True
            
            # Column win
            col_ind = square % 3
            col = [self.board[col_ind + i * 3] for i in range(3)]
            if all(spot == letter for spot in col):
                return True
            
            # Diagonal win
            if square % 2 == 0:
                # Descending diagonal win
                desc_diagonal = [self.board[i] for i in [0, 4, 8]]
                if all(spot == letter for spot in desc_diagonal):
                    return True
                
                # Ascending diagonal win
                asc_diagonal = [self.board[i] for i in [2, 4, 6]]
                if all(spot == letter for spot in asc_diagonal):
                    return True
            
            # If all checks fail we don't have a winner yet
            return False
    
    # Create next turn function
    def next_turn(self):
        self.player = 'X' if self.player == 'O' else 'O'


def play(game, x_player, o_player, print_game=True):
    # Print numbered board if print_game is toggled
    if print_game:
        game.print_board_nums()
    
    # Loop while game is still running or until a player wins
    while game.still_running():
        # Get move from the player whose turn it is
        letter = game.player
        square = x_player.get_move(game) if letter == 'X' else o_player.get_move(game)
        
        game.num_of_plays += 1
        game.make_move(square, letter)
        # Print the move and the board
        if print_game:
            print(f'{letter} makes a move to square {square}')
            game.print_board()
            print()
        
        # Check if player has won
        if game.current_winner is not None:
            print(f'{letter} won!')
            return letter
        
        # Alternate players
        game.next_turn()
        
        # Delay other player move to make it easier to read
        if print_game:
            time.sleep(0.6)
    
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player)