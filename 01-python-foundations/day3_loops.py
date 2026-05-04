# The Daemon Process - Write a while True loop that continuously asks the user for a server status
while True:
    status = input("Enter status: ").upper()
    if status == "OK":
        print("200 OK")
    elif status == "FAIL":
        print("502 Bad Gateway")
    elif status == "CRITICAL":
        print("!WARN!Server status is CRITICAL!")
        break
    else:
        print("Server Health-Check is In-Progress")
print()
# The Bottleneck
servers = ["app1","app2"]
regions = ["us-east","eu-west"]

for server in servers:
    for region in regions:
        print(f"{server} <> {region}")