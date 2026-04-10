#Build a script that scans a property portfolio, identifies "Active" listings, & automatically calculates
#the projected 3% commission for each.
portfolio = ["41026 Main St", "61718 Benson Way", "5038 Homie Ln", "3315 North Cir"]
house_1 = {'address': '41026 Main St', 'price':6_050_000, 'status':'Pending'}
house_2 = {'address': '61718 Benson Way', 'price':7_790_000, 'status':'Sold'}
house_3=  {'address': '5038 Homie Ln', 'price':9_500_000, 'status':'Active'}
house_4=  {'address': '3315 North Cir', 'price':8_500_000, 'status':'Active'}
office_listings = [house_1,house_2,house_3,house_4]

print("---Commencing Spring Commission Forecast---")
for house in office_listings:
    if house['status'] == 'Active':
        #Calculate 3% commission
        commission = house['price'] * 0.03
        #Task: Print the address and formatted commission
        print(f"Property: {house['address']}  | Projected Commission: ${commission:,.2f}  ")
print("---Forecast Complete---")