print("---System Initialized---")
property = "101 Rainey Street"
customer_name = input("What is your name?").title()
print(f"Welcome to the store, {customer_name}!")
movies_to_rent = int(input("How many movies would you like to rent today?"))
final_count = movies_to_rent
total_bill = final_count * 5
print(f"Perfect! for {final_count} movies at {property}, your total is ${total_bill}.")
if total_bill > 20:
    print("---VIP STATUS DETECTED---")
    print("Congratulations! You've earned a FREE bucket of popcorn!")
else:
    print("Thank You for your business! Have a great movie night.")
#example of "list"
movie_inventory = ["Sinners", "Leave the World Behind", "Friday", "Imitation of Life", "Django", "Inglorious Bastards"]
print(f"\nCurrently on the shelf: {movie_inventory}")
#For every [item] in the [inventory]
for movie in movie_inventory:
    #Be sure everything is tabbed in here happens for every movie
    print(f"Robot: Picking up '{movie}'...")
    print(f" Action: Stamping 'Inspected' on the case for {movie}. ")

print("\n---Audit Complete: All items on the shelf are ready for rent! ")
#List[] of dictionaries{}.This is how to show multiple items with prices
store_inventory = [{"title": "Sinners","format":"Blu-Ray","price":30,"is_available": True},
                {"title": "Leave the World Behind","format":"Blu-Ray","price": 20,"is_available": True},
                {"title": "Friday","format":"Blu-Ray","price": 20,"is_available": True},
                {"title": "Imitation of Life","format":"Blu-Ray","price": 10,"is_available": True},
                {"title": "Django","format":"Blu-Ray","price": 20,"is_available": False},
                {"title": "Inglorious Bastards","format":"Blu-Ray","price": 20,"is_available": True}]
print("\n---Detailed Inventory Report---")
#Display price for many opts,loop through the list[{}]
for item in store_inventory:
    #item represents the dictionary we are currently looking at
    name = item["title"]
    cost = item["price"]
    print(f"Movie: {name} | Price: ${cost}")
print("\n---End of Report---")



