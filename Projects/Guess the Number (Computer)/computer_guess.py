import math 
import random

def main():
    # Prompt user for lower and upper bound
    lower_bound = get_int('Enter lower bound: ')
    while True:
        upper_bound = get_int('Enter upper bound: ')
        # Check Upper bound is greater than lower bound
        if upper_bound > lower_bound:
            break
        print('Upper bound has to be greater than lower bound')

    # Declare user number of tries, correct answer and maximum number of tries
    tries = 0
    answer = random.randint(lower_bound, upper_bound)
    maximum_number_of_tries = round(math.log(upper_bound - lower_bound + 1, 2))

    print(f'You only have {maximum_number_of_tries} chances to guess the number!')

    while tries < maximum_number_of_tries:
        # Prompt user for a guess
        guess = int(input('Guess a number: '))
        # Check if user failed all tries
        if tries == maximum_number_of_tries - 1 and guess != answer:
            print(f'The correct answer is {answer}', 'Better Luck Next Time!', sep='\n')
            break
        # Check if user guess is greater than answer
        if guess > answer:
            print('Try Again. Too high.')
        # Check if user guess is smaller than answer
        elif guess < answer:
            print('Try Again. Too low.')
        # Check if user inputted the correct answer
        else:
            if tries == 0:
                print('Congratulations! you did it in 1 try')
                break
            print(f'Congratulations! you did it in {tries + 1} tries')
            break
        tries += 1


# Check user inputs integers
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter an integer')
            pass


if __name__ == '__main__':
    main()