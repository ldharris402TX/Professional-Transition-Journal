def calculate_commission(address, price):
    commission = price * 0.03
    return commission
heaven_comm = calculate_commission("777 Heaven St", 500_000)
main_comm = calculate_commission("1234 Main Cir", 850_000)
print(f"Total Company Revenue: ${heaven_comm + main_comm}")