# The RE Filing Cabinet
portfolio = ["777 Heaven Street", "112 Club Boom Boom Blvd", "4926 April Court"]
first_prop = {"address": "777 Heaven Street", "price": 450_000, "status": "Sold"}
second_prop = {"address": "112 Club Boom Boom Blvd", "price": 600_000, "status": "Available"}
third_prop = {"address": "4926 April Court", "price": 850_000, "status": "Pending"}

office_listings = [first_prop, second_prop, third_prop]
for house in office_listings:
    if house ['price'] < 500_000:
        print(f"High-Value Property Found: {house ['address']}")

    print("---Audit Complete---")


# Task: Print the address of any property where the price is > 500000
# Write your for loop and if statement here: