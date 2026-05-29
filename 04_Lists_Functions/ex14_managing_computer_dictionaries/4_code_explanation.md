> [!NOTE]
> 
> # CODE EXPLANATION:
> 
> 1. `Computers_1 = {`
`"Brand": "Asus",`
`"Screen": "14inch",`
`"RAM": [4, 8, 12]`
`}`
> - Creates a dictionary named `Computers_1 `with keys `"Brand"`, `"Screen"`, and `"RAM"`; `"RAM"` stores a list of integers.
> 
> 2. `Computers_1["Disk"] = ["128G", "256G"]`
> - Adds a new key `"Disk"` with a list of two strings as its value.
> 
> 3. `value = int(input("Enter a RAM value: "))` 
> - Reads a value from the user, converts it to an integer, and stores it in `value`.
> 
> 4. `if value in Computers_1["RAM"]:` 
> - Checks if `value` is present in the list stored under the `"RAM"` key.
>
> 5. `print("RAM exists")`
> - Prints this message if the value is found in the `"RAM"` list.
> 
> 6. `else:`
> - Defines the alternative path if the value is not found.
> 
> 7. `print("RAM not found")` 
> - Prints this message if the value is not in the `"RAM"` list.
> 
> 8. `Computers_1["RAM"].append(16)` 
> - Adds the integer `16` to the list stored under `"RAM"`.
>
> 9. `import copy`
> - Imports the `copy` module, which provides functions for copying objects.
> 
> 10. `Computers_2 = copy.deepcopy(Computers_1)`
> - Creates a deep copy of `Computers_1` and stores it in `Computers_2`. Changes to one will not affect the other.
> 
> 11. `Computers_2["Brand"] = "Lenovo"` 
> - Changes the value of the `"Brand"` key in `Computers_2` to `"Lenovo"`.
> 
> 12. `Computers_2["RAM"] = [4, 8]` 
> - Replaces the "RAM" list in `Computers_2` with a new list `[4, 8]`.
>
> 13. `print(Computers_2)` 
> - Prints the `Computers_2` dictionary.
>
> 14. `Computers_3 = copy.deepcopy(Computers_1)` 
> - Creates another deep copy of `Computers_1` and stores it in `Computers_3`.
> 
> 15. `Computers_3["Brand"] = "HP"` 
> - Changes the "Brand" value in `Computers_3` to `"HP"`.
>
> 16. `Computers_3["Disk"] = ["256G"]` 
> - Replaces the `"Disk"` list in `Computers_3` with a new list containing only `"256G"`.
>
> 17. `print(Computers_3)` 
> - Prints the `Computers_3` dictionary.
> 
> 18. `computers_list = [Computers_1, Computers_2, Computers_3]` 
> - Creates a list named `computers_list` containing the three dictionaries.
>
> 19. `for comp in computers_list:` 
> - Starts a loop that goes through each dictionary in `computers_list`, assigning each to `comp`.
>
> 20. `if "128G" in comp.get("Disk", []):` 
> - Uses get to retrieve the `"Disk"` list (or an empty list if `"Disk"` does not exist), then checks if `"128G"` is in that list.
> 
> 21. `print(comp["Brand"])` 
> - If the condition is true, prints the value of the `"Brand"` key for that dictionary.
>
> 22. `for comp in computers_list:` 
> - Starts another loop over each dictionary in `computers_list`.
>
> 23. `if 8 in comp["RAM"] and 12 in comp["RAM"]:` 
> - Checks if both `8` and `12` are present in the `"RAM"` list of the current dictionary.
>
> 24. `print(comp["Brand"])` 
> - If the condition is true, prints the brand of that computer.