# Exercise description:

## Managing Computer Dictionaries

- Write a program that:
  - Creates the dictionary:
  - `Computers_1 = {`
  -   `"Brand": "Asus",`
  -   `"Screen": "14inch",`
  -   `"RAM": [4, 8, 12]`
  - `}`

- Adds a new key `"Disk"` with the value `["128G", "256G"]`.
- Asks the user for a RAM value and checks whether it exists in the `"RAM"` list.
- Adds the value `16` to the `"RAM"` list.
- Creates a **deep copy** of the dictionary.
- In the copied dictionary, changes `"Brand"` to `"Lenovo"` and `"RAM"` to `[4, 8]`, then prints the updated dictionary.
- Creates another deep copy, changes `"Brand"` to `"HP"` and `"Disk"` to `["256G"]`, and prints the updated dictionary.
- Creates a **list** containing the three dictionaries.
- Prints the **brands** of computers that have `"128G"` in `"Disk"`.
- Prints the **brands** of computers that have **8 and 12** in `"RAM"`.
