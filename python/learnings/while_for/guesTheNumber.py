# this is the guess a number game
import random
secretNumber = random.randint(1, 20)
print("Computer: I'm thinking of a number between 1 and 20.")

# ask a player to guess 6 times
for guessesTaken in range(1, 7):
    print('Computer: Take a guess!', 'You have:', (- guessesTaken) + 7, 'guesses.')
    guess = int(input('Vladimir: '))

    if guess < secretNumber:
        print('Computer: Your guess is too low.')
    elif guess > secretNumber:
        print('Computer: Your guess is too high.')
    else:
        break   # this condition is thr correct guess

if guess == secretNumber:
    print('Computer: Good job! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Computer: Nope. The number I was thinking of was ' + str(secretNumber))