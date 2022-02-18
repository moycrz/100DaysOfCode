import random
import os
from art import logo


def random_number():
    number = random.randint(1, 100)
    return number


def play_game():
    answer = random_number()
    print(f"Pssst, the correct answer is {answer}")
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficult == "easy":
        turns = 10
    elif difficult == "hard":
        turns = 5
    
    print(f"You have {turns} attempts remaining to guess the number.")

    while turns >= 0:
        guess = int(input("Make a guess: "))
    
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            break        
        elif guess < answer:
            print("Too low.")
            turns -= 1
            print(f"You have {turns} attempts remaining to guess the number.")
        elif guess > answer:
            print("Too high.")
            turns -= 1
            print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You've run out of guesses, you lose.")
        
        


if __name__ == '__main__':
    os.system("clear")
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    play_game()