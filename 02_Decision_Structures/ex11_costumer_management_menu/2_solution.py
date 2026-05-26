# Customer Management Menu using match/case

print("***** Customer List *****")
print("1 – Add Customer")
print("2 – Edit Customer")
print("3 – Delete Customer")
print("4 – Exit Program")

option = int(input("Enter your option: "))

match option:
    case 1:
        print("You selected option 1")
    case 2:
        print("You selected option 2")
    case 3: 
        print("You selected option 3")
    case 4:
        print("You selected option 4")
    case _:
        print("Invalid option.")