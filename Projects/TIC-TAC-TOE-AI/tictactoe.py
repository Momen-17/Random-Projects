from player import *


class TicTacToe:
    def __init__(self):
        self.player = 'X' # X or O
        self.current_winner = None # Track the winner
        self.board = [' ' for _ in range(9)] # Create the board
    
    # Print the state of the board
    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # Print the numbered board
    @staticmethod
    def print_board_nums():
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    # The indices of all available squares
    def available_squares(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    # Implement the still running method
    def still_running(self):
        return ' ' in self.board # Boolean expression
    
    # Implement the make move method
    def make_move(self, square, player):
        # Assign the letter to the square
        self.board[square] = player
        # Check if player won
        if game.winner(square, player, self.board):
            self.current_winner = player
    
    # Implement the winner method
    def winner(self, square, player, board):
        if board.count(' ') <= 5:
            # Row win
            row_ind = square // 3
            row = board[row_ind * 3: (row_ind + 1) * 3]
            if all(spot == player for spot in row):
                return True
            
            # Col win
            col_ind = square % 3
            col = [board[col_ind + i * 3] for i in range(3)]
            if all(spot == player for spot in col):
                return True
            
            # Diagonal win
            if square % 2 == 0:
                # Descending diagonal
                desc_diagonal = [board[i] for i in [0, 4, 8]]
                if all(spot == player for spot in desc_diagonal):
                    return True
                
                # Ascending diagonal
                asc_diagonal = [board[i] for i in [2, 4, 6]]
                if all(spot == player for spot in asc_diagonal):
                    return True
        
        # If all checks fail then we don't yet have a winner
        return False
    
    # Implement the next turn method
    def next_turn(self):
        self.player = 'X' if self.player == 'O' else 'O'


def play(game, x_player, o_player, print_board=True):
    if print_board:
        game.print_board_nums()
    
    # Loop while game is still running or a player has won
    while game.still_running():
        player = game.player
        square = x_player.get_move(game) if player == 'X' else o_player.get_move(game)
        
        game.make_move(square, player)
        
        if print_board:
            print(f'{player} makes move to square {square}')
            game.print_board()
            print()
        
        if game.winner(square, player, game.board):
            if print_board:
                print(f'{player} won!')
            return player
        
        game.next_turn()
    
    if print_board:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        game = TicTacToe()
        x_player = HumanPlayer('X')
        o_player = UnbeatableAIPlayer('O')
        result = play(game, x_player, o_player, False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    
    print(f'X: {x_wins}, O: {o_wins}, Ties: {ties}')
