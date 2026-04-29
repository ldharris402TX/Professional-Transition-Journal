print("--- Initializing Rent Roll Audit ---")

# 1. THE DATA (List of Dictionaries)
portfolio = [
    {"unit": "101", "tenant": "Smith", "rent": 1200},
    {"unit": "102", "tenant": "Johnson", "rent": 1500},
    {"unit": "103", "tenant": "Williams", "rent": 2100}
]

# 2. THE BLANK PAPER
total_revenue = 0

# 3. THE LOOP
for unit in portfolio:
    # Extract the rent amount from the dictionary
    current_rent = unit["rent"]

    # Add it to the total
    total_revenue = total_revenue + current_rent

# 4. THE OUTPUT (Outside the loop!)
print(f"Total Monthly Revenue: ${total_revenue}")