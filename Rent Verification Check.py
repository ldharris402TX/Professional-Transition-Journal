print("Welcome to the Rent Check!")
monthly_income = int(input("Enter your monthly income: "))
monthly_rent = int(input("Enter the monthly rent: "))
required_income = monthly_rent * 3

if monthly_income >= required_income:
    print("Success: You make enough! Move-in Ready.")
else:
    difference = required_income - monthly_income
    print(f"Wish we could help: You need ${difference} more per month to qualify.")