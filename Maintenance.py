#Goal: Create a script that determines the dispatch level for a repair request based on time and severity.
name = input("What is your name?").title()
address = input("What is your unit address?")
issue = input("What is the maintenance issue?").lower()
time = input("Is it after 5P CST? Yes/No").lower()
emergency = input("Is this a maintenance life/safety emergency? Yes/No").lower()
# Change "Yes" to "yes" and "No" to "no" to match your .lower() inputs
if issue == "fire" or emergency == "yes":
    print(f"Hello {name.title()} at {address}.CRITICAL:Call 911 immediately and \nNotify Building Owner immediately!")
elif issue == "leak" and time == "yes":
    print(f"Hello {name.title()} at {address}.URGENT: Dispatch On-Call Plumber (Emergency Rates Apply)")
elif time == "no":
    print(f"Hello {name.title()} at {address}. ROUTINE: Schedule with in-house maintenance for tomorrow.")
else:
    print(f"Hello {name.title()} at {address}. LOGGED: Maintenance request recorded for review.")