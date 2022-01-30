print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = (int(input("What percentage tip would you like to give? 10, 12, or 15? ")))/100
n_people = int(input("How many people to split the bill? "))

total = round(((bill * (1+percentage))/n_people), 2)

print(f"Each person should pay: ${total}")