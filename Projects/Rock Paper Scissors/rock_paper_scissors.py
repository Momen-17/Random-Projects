import random

def main():
    # Loop until one wins
    while True:
        while True:
            # Prompt user for move
            user = input("'R' for rock, 'P' for paper, and 'S' for scissors: ").upper()
            # Check move validation
            if user in ['R', 'P', 'S']:
                break
            print("Please enter 'R', 'P', or 'S'")
        computer = random.choice(['R', 'P', 'S'])
        
        print(f'You vs Computer: {user} vs {computer}')
        
        # Check if it's a tie
        if user == computer:
            print('Tie! try again.')
            pass
        # Check if user won
        if (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
            return print('You won. Congratulations!')
        # Otherwise user lost
        return print('You lost. Good luck next time!')


if __name__ == '__main__':
    main()