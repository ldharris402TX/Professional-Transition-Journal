#Tenant Screening Drill
monthly_rent = 2500
deposit_factor = 1.5
admin_fee = 250
tenant_savings = 6000
security_deposit = monthly_rent * deposit_factor
total_required = monthly_rent + security_deposit + admin_fee

print(f"---AUDIT FOR UNIT 101---")
print(f"Total Funds Required: ${total_required}")
print(f"Tenant Funds Available: ${tenant_savings} ")

if tenant_savings >= total_required:
    print("RESULT: PASSED. Move-in authorized!")
else:
    short_fall = total_required - tenant_savings
    print(f"RESULT: FAILED. Tenant is short by ${short_fall}")