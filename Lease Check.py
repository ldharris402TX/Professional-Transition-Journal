#Drill to help with skills and memorization
print("---Lease Balance Verify---")
first_name = input("What is your first name?").title()
address = input("What is your address?").title()
outstanding_balance = float(input("What is your balance?"))
print("\n---Processing Account Status---")
if outstanding_balance > 0:
    print(f"ALERT:{first_name}, the account for {address} has an outstanding balance of ${outstanding_balance}")
    print("ACTION REQUIRED: Please send a payment reminder.")
else:
    print(f"SUCCESS: {first_name}, the account for {address} is fully paid. Balance is $0.00.")