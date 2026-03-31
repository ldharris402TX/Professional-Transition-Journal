print("Welcome to the deposit calculator! ")
monthly_rent = float(input("What is the monthly rent?"))
credit_score = int(input("What is the tenant's credit score?"))

if credit_score >= 700:
    deposit = monthly_rent * 0.5
    print(f"Excellent Credit: Deposit is only ${deposit}")
elif credit_score >= 600:
    deposit = monthly_rent * 1.0
    print(f"Approved Credit: Deposit is ${deposit}")
else:
    deposit = monthly_rent * 2.0
    print(f"Risk Alert: Double Deposit required ${deposit}")