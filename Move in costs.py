#RE multiplication drills
applicant_name = input("What is your name?")
unit_address = input("What is the unit address?")
monthly_rent = 2200
deposit = 1.5
cleaning_fee = 300
security_deposit = monthly_rent * deposit
total_deposit_due = monthly_rent + security_deposit + cleaning_fee
print(f"Good Day {applicant_name}, for address {unit_address}. The monthly rent is ${monthly_rent} \n security deposit is ${security_deposit}, cleaning fee ${cleaning_fee}. The total due at lease signing is ${total_deposit_due}.")