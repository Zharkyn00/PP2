import json

file_path = r"C:\Users\User\Desktop\lab4\sample-data.json"
with open(file_path, "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<45} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else "inherit"
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print("{:<45} {:<15} {:<10} {:<10}".format(dn, description, speed, mtu))