from words import random_word


def main():
    lives = 6
    guessed = set()
    answer = random_word()
    char_list = ['-' for _ in answer]
    
    while lives > 0:
        # Display game status
        print(f'You have {lives} lives left and used these letters: {" ".join(guessed)}')
        print(f'Current word: {" ".join(char_list)}\n')
        while True:
            # Prompt user for a letter guess
            guess = input('Guess a letter: ').upper()
            
            # Validate user's input
            if guess.isalpha() and len(guess) == 1:
                break
            print('Please enter a single alphabetical letter.')
        
        # Check if user already used the letter
        if guess in guessed:
            print(f'You have already used the letter {guess}.')
            continue
        
        guessed.add(guess)
        # Check if user guessed an incorrect letter
        if guess not in answer:
            lives -= 1
            print(f'Letter ({guess}) is not in the word.')
            continue
        
        # Change the current word if user guessed correctly
        for i, letter in enumerate(answer):
            if guess == letter:
                char_list[i] = guess
        
        # Check if user has correctly guessed all letters
        if '-' not in char_list:
            return print('Congratulations! You have correctly guessed the word', answer)
    
    print('You died. The word was:', answer)


if __name__ == '__main__':
    main()
