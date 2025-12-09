print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
choice = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total =  (bill * (choice/100) + bill) / people
print(f"Each person should pay: ${round(total,2)}")