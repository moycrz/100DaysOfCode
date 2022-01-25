import os

def prime_number(check_number):
    if check_number == 1:
        return True
        #return f"{check_number}, it's not a prime number"

    else:
        count = 0
        prime = [i for i in range(1, check_number + 1) if check_number % i == 0]
        if  len(prime) == 2:
            return True
            #return f"{check_number}, it's a prime number"
        else:
            return False
            #return f"{check_number}, it's not a prime number"

if __name__ == "__main__":
    os.system('clear')
    prime_true = []
    prime_false = []
    #usr_choose = int(input("Write the number you want to check: "))
    for i in range(0, 101):
        #usr_choose = i
        if prime_number(i):
            prime_true.append(i)
        else:
            prime_false.append(i)

    print(f"{prime_true}, it's prime")
    print(f"{prime_false}, it's not a prime")

    #print(prime_number(usr_choose))