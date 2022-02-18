from socket import timeout
from art import logo
import os
import time


def comprobation(a, b, operation):
    if operation == "+":
        return a + b


    elif operation == "-":
        return a - b   

    
    elif operation == "*":
        return a * b

    
    elif operation == "/":
        return a / b
    

if __name__ == "__main__":
    
    while True:
        os.system("clear")
        print(logo)
        firs_number = float(input("What's the first number?: "))
        op = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))

        print(f"{firs_number} {op} {second_number} = {comprobation(firs_number, second_number, op)}")
        ans = input("Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: ")

        if ans == "y":
            continue

        elif ans == "n":
            break
        
        else:
            print("Value out of range, restarting ...")
            time.sleep(2)
