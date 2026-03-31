print("Welcome to the Lease Screener!")
credit_score = int(input("What is the tenants credit score? "))
has_cosigner = input("Does the tenant need a co-signer? (yes/no): ")
if credit_score >= 700 and has_cosigner == "no":
    print("Result: Gold Tier. Approve Immediately!")
elif credit_score >= 600 or has_cosigner == "yes":
    print("Result: Conditional Approval. Needs a managers signature.")
else:
    print("Result: Denied. Does not meet minimum requirements.")