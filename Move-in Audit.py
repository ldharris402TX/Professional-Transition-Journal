monthly_rent = 2000
deposit = 3750
admin_fee = 250
tenant_savings = 1000
total_required = monthly_rent + deposit +admin_fee
print(f"---TIERED AUDIT RESULTS---")
#The "if"statement needs to have the most difficult requirement at the top
if tenant_savings >= total_required:
    print("Status: Full Approval")
    print("Action: Issue keys immediately!")
#Conditional-Middle Ground can have as many "elif" statements as necessary
elif tenant_savings >= (monthly_rent + admin_fee):
    print("Status: Conditional Approval")
    print("Action: Set-up 3 month payment plan for Security Deposit.")
#Catch all if the statement isnt true for "if" & "elif" "else" catches the logic-False
else:
    print("Status: Denied")
    print("Action: Refer to credit counseling or low income housing.")
