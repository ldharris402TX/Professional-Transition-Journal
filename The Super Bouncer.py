has_id = False
has_ticket = False
is_wearing_fancy_shoes = True
print("---Checking the Nightclub Entrance---")

if has_id == True and has_ticket == True:
    print("Welcome! You have your ID and your ticket.")
elif is_wearing_fancy_shoes == True or has_ticket == True:
    print("You're in! (Either your fancy or you paid).")
elif is_wearing_fancy_shoes:
    print("Wait! You aren't wearing fancy shoes, but we'll let it slide.")
else:
    print("Sorry, you need Both your ID and your ticket to enter.")