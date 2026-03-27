monthly_rent = 2000
days_late = 45
repeat_offender = False
daily_fee = 50
total_late_fees = days_late * daily_fee
print("---Late Fee Audit---")

if days_late > 5 and repeat_offender == True:
    grand_total = total_late_fees + 100
    print(f"Status: Heavy Penalty. Total due: ${grand_total}")
elif days_late > 0:
    print(f"Status: Standard Penalty. Total due: ${total_late_fees}")
else:
    print("Status: One Time. No fees!")