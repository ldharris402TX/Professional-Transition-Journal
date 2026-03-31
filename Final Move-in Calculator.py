print("Welcome to Move-in fee calculator!")
income = int(input("Monthly Income: "))
credit = int(input("Credit Score: "))
rent = float(input("Monthly Rent: "))
is_student = input("Are you a student? (yes/no): ").title()
is_senior = input("Are you 65 years or better? (yes/no): ").title()
#the and rule, both need to be "true"
if income >= (rent * 3) and credit >= 650:
    print("---Access Granted---")
    #Starting math: Rent + $500 Security Deposit
    total_due = rent + 500.00
    #a nested "if" statement inside an "if" statement
    if is_student == "yes" or is_senior == "yes":
        print("Discount Applied: $200Credit for Special Status!")
        total_due = rent - 200.00
        print(f"Your total move-in cost is: ${total_due}")
else:
        print("---Access Denied---")
        print("Reason: Income or Credit Score too low.")
