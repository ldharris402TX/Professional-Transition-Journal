#Python drill for memorization
client_name = "Sarah Homebuyer"
print("---LEVEL 2: VARIABLES---")
print(f"Welcome to ABC Brokerage, {client_name}.\n")
active_buyers_list = ["Sarah Homebuyer", "Michael Seller", "David Investor"]

print("---LEVEL 3: LISTS---")
print(f"All active buyer: {active_buyers_list}")

first_buyer = active_buyers_list[0]
print(f"The first buyer in line is: {first_buyer}\n")
client_profile = ({"name": "Sarah Homebuyer", "budget": "$550,000", "zip_code": "78745"},
                  {"name": "Michael Seller", "budget": "$750,000", "zip_code": "78642"},
                  {"name": "David Investor", "budget": "$300,000", "zip_code": "78704"})
print("---LEVEL 4: DICTIONARIES---")
sarah_budget = client_profile [0]["budget"]
print(f"The budget stored for Sarah in our dictionary is: {sarah_budget}")
sarah_zip = client_profile [0]["zip_code"]
print(f"The zip code stored for Sarah in our dictionary is: {sarah_zip}")