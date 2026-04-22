print("---AWS EC2 Health Scanner Initialized---\n")
#the data
ec2_fleet = [{"server_name": "Tenant Portal Web","Status": "Running"},
             {"server_name": "Database Backup", "Status": "Stopped"},
             {"server_name": "Payment Gateway", "Status": "Crashed"}]
#the scanner, looping
for server in ec2_fleet:
    name = server["server_name"]
    current_status = server["Status"]
    #the decision engine
    if current_status == "Running":
        print(f"STATUS OK:{name} is online and serving tenants.")
    elif current_status == "Stopped":
        print(f"ACTION REQUIRED:{name} is offline. Rebooting instance...")
    else:
        print(f"CRITICAL ALERT:{name} has experienced a fatal error. Paging engineer!")
print("\n---SCAN COMPLETE---")