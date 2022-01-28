import os
from Day_9_art import logo

def add_bidders():
    there_are_bidders = True
    bidders = {}

    while there_are_bidders:
        os.system("clear")
        print(logo)
        name = input("What is your name?: ")
        offert = input("What is your bid?: $")
        bidders [name] = offert

        usr_answer = input("Are there any other bidders? Type 'yes or 'no': ").lower()
        if usr_answer == "no":
            find_highest_bidder(bidders)
            there_are_bidders = False

        else:
            continue


def find_highest_bidder(bidders):
    highest_bidder = 0

    for key in bidders:
        score = int(bidders[key])

        if score > highest_bidder:
            highest_bidder = score
            higher_name = key
        else:
            continue

    print(f"The winner is {higher_name} with a bid of ${highest_bidder}")


if __name__ == "__main__":
    add_bidders()