#########################
# Guess the number game #
#########################
import random

# Here I will guess the computer's number.
def user_guess(x): 
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: # When guess is less than the selected number it will print.
            print('Sorry, guess again. Too low.')
        if guess > random_number: # When guess is greater than the selected number it will print.
            print('Sorry, guess again. Too high.')
    print(f'Hurrah! You have guessed the number {random_number} correctly') # When the guess is accurate


# Here computer will guess my number
def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high: # To check whether computer gets a range to look for the number because the range of low and high is changing after each iteration basis on the feedback. At the begining it start from low = 1, high = x
            guess = random.randint(low, high)
        else:
            guess = low # Could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Hurrah! The computer guessed your number, {guess}, correctly!')

# Game1
user_guess(10) #Limited guess from 1 to 10. 
# Game2
computer_guess(10)
