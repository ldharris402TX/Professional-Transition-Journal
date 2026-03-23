#Warm-ups from Gemini AI
print("Hello, Welcome to the Lease Vetter!")
name = input("What is your name?")
unit_address = input("What is the address of the unit?")
credit_score = int(input("What is your credit score?"))
income = float(input("What is your monthly income?"))
rent = float(input("What is your monthly rent?"))

if income >= 3600.00 and credit_score >= 700:
        print(f"Congratulations{ name.title()}, you are approved for the unit{unit_address}!\n at $1200.00 per month!")
elif income >= 3600.00 and credit_score <= 699:
    print(f"Hello {name.title()}, Your application has been denied. You may meet either the income or credit score requirement \n but not both.")
else:
    print(f"Hello {name.title()}, Your application has been denied. You must meet the Requirements: \n 3 times Rent Income and 700+ Credit Score.")