import random

def main():
    print('Think of a random number between x and y')
    # Get lower and upper bound from user
    x, y= get_int('x: '), get_int('y: ')
    
    feedback = ''
    # Loop until computer guess the correct answer
    while feedback != 'C':
        guess = random.randint(x, y)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').upper()
        
        # Check if computer guess is too low
        if feedback == 'L':
            x = guess + 1
        # Check if computer guess is too high
        elif feedback == 'H':
            y = guess - 1
    
    # Computer has guessed the correct answer
    print(f'The computer has guessed your number ({guess}) correctly!')


# Check user inputs integers
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print('Please enter an integer')


if __name__ == '__main__':
    main()