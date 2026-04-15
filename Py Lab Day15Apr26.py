print("--- Automated Showing Scheduler ---\n")
listings = [
    {"address": "777 Heaven St", "price": 1_000_000},
    {"address": "112 Club Boom Boom Blvd", "price": 450_000},
    {"address": "4926 April Court", "price": 850_000}
]
for house in listings:

    current_address = house["address"]
    current_price = house["price"]
    commission = current_price * 0.03

    if commission >= 20000:
        print(f"VIP SHOWING SCHEDULED: {current_address} requires luxury prep. Est Commission: ${commission:,.2f}")
    else:
        print(f"STANDARD SHOWING scheduled for {current_address}. Est Commission: ${commission:,.2f}")
print("\n--- All properties prepped ---")