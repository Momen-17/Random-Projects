board = ['-' for _ in range(9)]
current_player = 'X'
current_winner = None
game_running = True

def main():
    while game_running:
        print_board(board)
        player_move()
        did_player_win()
    print_board(board)
    print(f'Player {current_winner} Won' if current_winner in ['X', 'O'] else current_winner)


def print_board(board):
    for row in [board[i * 3: (i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


def player_move():
    global current_player
    
    if current_player == 'X':
        while True:
            x = int(input('X turn. Enter a move from 1-9: '))
            if x not in range(1, 10):
                print('Please enter a number in range of 1-9')
                continue
            if board[x - 1] == '-':
                board[x - 1] = 'X'
                break
            print('Please choose another move. Spot is taken!')
            print_board(board)
        current_player = 'O'
    elif current_player == 'O':
        while True:
            o = int(input('O turn Enter a move from 1-9: '))
            if o not in range(1, 10):
                print('Please enter a number in range of 1-9')
                continue
            if board[o - 1] == '-':
                board[o - 1] = 'O'
                break
            print('Please choose another move. Spot is taken!')
            print_board(board)
        current_player = 'X'


def did_player_win():
    global board, current_player, current_winner, game_running
    if board[0] == board[1] == board[2] != '-' or \
        board[3] == board[4] == board[5] != '-' or \
        board[6] == board[7] == board[8] != '-' or \
        board[0] == board[3] == board[6] != '-' or \
        board[1] == board[4] == board[7] != '-' or \
        board[2] == board[5] == board[8] != '-' or \
        board[0] == board[4] == board[8] != '-' or \
        board[2] == board[4] == board[6] != '-':
        current_winner = 'X' if current_player == 'O' else 'O'
        game_running = False
    elif '-' not in board:
        current_winner = 'Tie game'
        game_running = False


if __name__ == '__main__':
    main()