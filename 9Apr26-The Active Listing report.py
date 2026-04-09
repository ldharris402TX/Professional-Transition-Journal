#This is how you generate a "Shown List" for a buyer who only wants to see available homes.
# The RE Filing Cabinet
print("\n---Generating Showing Report---")
portfolio = ["777 Heaven Street", "112 Club Boom Boom Blvd", "4926 April Court", "4825 April Court"]
first_prop = {"address": "777 Heaven Street", "price": 450_000, "status": "Sold"}
second_prop = {"address": "112 Club Boom Boom Blvd", "price": 600_000, "status": "Available"}
third_prop = {"address": "4926 April Court", "price": 850_000, "status": "Pending"}
fourth_prop = {"address": "4825 April Court", "price": 1_850_000, "status": "Available"}

office_listings = [first_prop, second_prop, third_prop, fourth_prop]
for house in office_listings:
    if house ['status'] == "Available":
        print(f"Listing ready to show: {house ['address']} |  ${house ['price']:,} | {house ['status'] }")

print("---End of Report---")