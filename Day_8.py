def prime_number(check_number):
    if check_number == 1:
        return "{check_number} it's not a prime number"

    else:
        count = 0
        for i in range(1, check_number + 1):
            if check_number % i == 0:
                count += 1
            else:
                continue

        if count >= 2:
            return f"{check_number}, it's not a prime number"

        elif count ==2:
            return f"{check_number}, it's a prime number"

if __name__ == "__main__":
    usr_choose = input("Write the number you want to check: ")
    prime_number(usr_choose)