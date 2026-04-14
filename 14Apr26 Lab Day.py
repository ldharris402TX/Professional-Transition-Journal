print("Here is your preferred house!")
listings = ["777 Heaven St", "112 Club Boom Boom Blvd"]
user_name = input("What is your name?").title()
prop_address = input("What is the property address?").title()
client_name = input("What is the buyer clients name?").title()
house_price = float(input("What is the house list price?"))
commission = house_price * 0.03
if commission >= 20_000:
    print(f"LUXURY ALERT: High-commission showing with {client_name}.")
else:
    print(f"Standard showing with {client_name}.")
#Add new address to the basket from user input
listings.append(prop_address)
#Find out how many houses we have now including house from user input
total_listings = len(listings)
print(f"Hello { user_name}! The showing for {prop_address} is ready.\nThe home is priced at ${house_price:,.2f}. Est.commission ${commission:,.2f}.")
print("\n---Updated Showing Itinerary")
print(f"Current List:{listings}")
print(f"{user_name}, you have {total_listings} properties scheduled for today.")