age = 6
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2
print ("Your age is", age)
print("Day is", day)
if age > 40:
    price = 89
print("Ticket price for you is $",price)
print("Enjoy the show!")

# To commit code in git, follow these steps in your terminal:
# 1. Initialize git (if not already): git init
# 2. Add your changes: git add 02_solution.py
# 3. Commit your changes: git commit -m "Add ticket price calculation"