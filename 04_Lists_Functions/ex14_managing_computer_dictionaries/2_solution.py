# initial dictionary
Computers_1 = {
    "Brand": "Asus",
    "Screen": "14inch",
    "RAM": [4, 8, 12]
}

# add Disk
Computers_1["Disk"] = ["128G", "256G"]

# ask for RAM value
value = int(input("Enter a RAM value: "))

# check if RAM exists
if value in Computers_1["RAM"]:
    print("RAM exists")
else:
    print("RAM not found")

# add new RAM value
Computers_1["RAM"].append(16)

# deep copy
import copy
Computers_2 = copy.deepcopy(Computers_1)

# modify copy
Computers_2["Brand"] = "Lenovo"
Computers_2["RAM"] = [4, 8]
print(Computers_2)

# second deep copy
Computers_3 = copy.deepcopy(Computers_1)

# modify second copy
Computers_3["Brand"] = "HP"
Computers_3["Disk"] = ["256G"]
print(Computers_3)

# list of dictionaries
computers_list = [Computers_1, Computers_2, Computers_3]

# print brands with 128G disk
for comp in computers_list:
    if "128G" in comp.get("Disk", []):
        print(comp["Brand"])

# print brands with 8 and 12 RAM
for comp in computers_list:
    if 8 in comp["RAM"] and 12 in comp["RAM"]:
        print(comp["Brand"])