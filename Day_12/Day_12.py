from itertools import count
from art import logo




def check_answer(guess, answer, turns):
    count = turns

    while turns >= count:
        if guess == answer:
            pass        
        elif guess < answer:
            print("Too low.")
        elif guess > answer:
            print("Too high.")
        elif guess == answer - 5 or guess == answer - 4 or guess == answer - 3:
            print("Close, a little more")
        elif guess == answer + 5 or guess == answer + 4 or guess == answer + 3:
            print("Close, a little less")
        elif guess == answer - 2 or guess == answer -1:
            print("Very close ↑")
        elif guess == answer + 2 or guess == answer + 1:
            print("Very close ↓")
        
        count -= 1
        return count


def play_game():
    game = True
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficult == "easy":
        while game:
            print(f"You have {count} attempts remaining to guess the number.")
            check_answer(turns = 10)

    if difficult == "hard":
        while game:
            print(f"You have {count} attempts remaining to guess the number.")
            turns = 5

    







if __name__ == '__main__':
    check_answer()