print("Welcome to the Maintenance Portal!")
#Using a mix of text, numbers and multiple logic keys
issue = input("What is the issue? (flood, fire, or broken sink): ").lower()

#Fire or flood code red
if issue == "fire" or issue == "flood":
    print("---Sorting Your Request---")
    print("Priority: Code Red!")
    print("Action: Dispatch emergency team immediately.")

else:
    is_vip = input("Are you a VIP tenant? (yes/no): ").lower()
    hours_waiting = int(input("How many hours have you been waiting? "))

    print("---Sorting Your Request---")

    if is_vip == "yes" and hours_waiting >= 4:
        print("Priority: Code Blue. ")
        print("Action: Move to the top of the standard list.")
    else:
        print("Priority: Code Green.")
        print("Action: Maintenance will visit within 24 hours. ")