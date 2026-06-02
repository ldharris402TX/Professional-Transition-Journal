#Drill practice 2June
name = "Kendra"
buyer_name = input("What is your name?")
active_buyers = {
    "Buyer_One":{"budget": "$550,000", "zip_code": "78745"},
    "Buyer_Two":{"budget": "$280,000", "zip_code": "78660"}}
for buyer_name, info in active_buyers.items():

    print(f"Hi {name}! For {buyer_name}, we are searching for homes in {info['zip_code']} with a budget of {info['budget']}.")
