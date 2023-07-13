class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(9)]
        self.current_player = 'X'
        self.current_winner = None
        self.game_running = True

    def main(self):
        while self.game_running:
            self.print_board()
            self.player_move()
            self.check_winner()
        self.print_board()
        print(f'Player {self.current_winner} won' if self.current_winner in ['X', 'O'] else 'Tie game')

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def player_move(self):
        if self.current_player == 'X':
            while True:
                x = int(input('X turn. Enter a move from 1-9: '))
                if x not in range(1, 10):
                    print('Please enter a number in the range of 1-9')
                    continue
                if self.board[x - 1] == '-':
                    self.board[x - 1] = 'X'
                    break
                print('Please choose another move. Spot is taken!')
                self.print_board()
            self.current_player = 'O'
        elif self.current_player == 'O':
            while True:
                o = int(input('O turn. Enter a move from 1-9: '))
                if o not in range(1, 10):
                    print('Please enter a number in the range of 1-9')
                    continue
                if self.board[o - 1] == '-':
                    self.board[o - 1] = 'O'
                    break
                print('Please choose another move. Spot is taken!')
                self.print_board()
            self.current_player = 'X'

    def check_winner(self):
        if self.board[0] == self.board[1] == self.board[2] != '-' or \
                self.board[0] == self.board[3] == self.board[6] != '-' or \
                self.board[3] == self.board[4] == self.board[5] != '-' or \
                self.board[6] == self.board[7] == self.board[8] != '-' or \
                self.board[1] == self.board[4] == self.board[7] != '-' or \
                self.board[2] == self.board[5] == self.board[8] != '-' or \
                self.board[0] == self.board[4] == self.board[8] != '-' or \
                self.board[2] == self.board[4] == self.board[6] != '-':
            self.current_winner = 'X' if self.current_player == 'O' else 'O'
            self.game_running = False
        elif '-' not in self.board:
            self.current_winner = 'Tie game'
            self.game_running = False


if __name__ == '__main__':
    game = TicTacToe()
    game.main()
