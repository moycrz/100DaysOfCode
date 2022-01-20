#Password Generator Project
import random
import os
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

os.system("clear")
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwd = []

for i in range(0, nr_letters):
    passwd.append(letters[random.randint(0, len(letters)-1)])

for i in range(0, nr_symbols):
    passwd.append(symbols[random.randint(0, len(symbols)-1)])  

for i in range(0, nr_numbers):
    passwd.append(numbers[random.randint(0, len(numbers)-1)])

passwd_unsort = "".join(random.sample(passwd, len(passwd)))
passwd = "".join(passwd) # la funcion .join() convierte una lista en str 

if sys.platform.startswith('linux'):
    os.system("clear")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.system("cls")


print(f"\n\tYour password is: {passwd_unsort}")