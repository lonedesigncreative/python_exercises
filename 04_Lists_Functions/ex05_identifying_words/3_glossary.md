# 1 - Print

## What it is:  
`print` is a command that shows something on the screen.

> [!CAUTION]
> - **Always use parentheses** → print("Hello")
> - Text must be inside quotes `" "`
> - Missing quotes or parentheses causes an error.

**Example:**
`print("Python!")`

This will display:
- *Python!*

# 2 - Text (in Python called string)

## What it is:  
Text inside quotes `" "`.

> [!CAUTION]
> - Text must always be inside quotes.
> - If you put numbers inside quotes, they become text, not numbers.

**Example:**
`name = "LoneDesign"`

# Summary

| **Concept** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| print | hows something on the screen | print("Hi") |
| integer | Whole number | 10 |
| decimal (float) | Number with decimal | 2.5 |
| text (string) | Words inside quotes | "Hello" |



# 2 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 3 - { }
## What it means:
The `{ }` are used to show the value of a variable inside the text.

> [!CAUTION]
> - Inside `{ }` you must put a **variable** or an **expression**.
> - If you put text without quotes, it gives an error.
> - If you put quotes inside `{ }`, it becomes text again.

**Example:**
`age = 25`
`print(f"You are {age} years old")`

Python replaces {age} with the value of the variable.

# Summary

| **Concept** | **Meaning** | **Example** |
| :---: | :--- | :---: |
| input | Asks the user to type something | `input("Your name: ")` |
| f-string | Text that can show variables | `f"Hello {name}"` |
| { } | Shows the variable’s value inside the f string | `{age}` |


# 4 - [ ]

## What it means:
In Python, **square brackets** `[]` are used for **three main things**:
  1. Creating lists
  2. Accessing elements by index
  3. Slicing lists or strings

> [!IMPORTANT]


> ### 1. [] to create a list
> - A **list** is a collection of items.
> 
> `numbers = [1, 2, 3, 4]`
> `fruits = ["apple", "banana", "orange"]`
> `mixed = [10, "hello", True]`
> 
> ### 2. [] to access an element (indexing)
> - Indexes start at **0**.
> 
> `fruits = ["apple", "banana", "orange"]`
> 
> `print(fruits[0])`   # apple
> `print(fruits[1])`   # banana
> `print(fruits[2])`   # orange
> 
> - Negative indexes count from the end:
> 
> `print(fruits[-1])`  # orange
> 
> ### 3. [] to slice (get a part of a list or string)
> 
> `numbers = [10, 20, 30, 40, 50]`
> 
> `print(numbers[1:4])`   # [20, 30, 40]
> `print(numbers[:3])`    # [10, 20, 30]
> `print(numbers[2:])`    # [30, 40, 50]
> 
> - Works with **strings** too:
> 
> `text = "Python"`
> `print(text[0:3])`   # Pyt

> [!NOTE]
> ### 4. Other uses of []
> **4.1 - Empty list**
> `empty = []`
>
> **4.2 - List inside a list (nested list)**
> `matrix = [[1, 2], [3, 4]]`
> 
> > **4.3 - Adding items**
> `fruits.append("kiwi")`

> [!CAUTION]
> - **Index starts at 0** → `fruits[0]` is the first item.
> - **Index out of range error** → `fruits[10]` gives an error.
> - **Lists are mutable** → you can change items inside them.
> - **Slicing creates a copy** → modifying the slice doesn’t change the original list.
> - **Use [] for lists, not ()** → parentheses are for tuples.


# 5 - Min()

## What it is:  
`min` is a **built‑in Python function** that returns the **smallest value** in an iterable (list, tuple, set, etc.) or among multiple values.

>> “Give me the smallest element.”

> [!NOTE]
> ### Basic structure:
> **Using an iterable**
>    - `min(iterable)`
> **Using multiple values**
>    - `min(value1, value2, value3)`

> [!IMPORTANT]
> **## How `min` works**
> - With **numbers** → returns the lowest number
> - With **strings** → returns the first alphabetically
> - With **mixed types** → ❌ error
> - With **empty iterables** → ❌ error


> [!TIP]
> **## Using `min` with dictionaries**
> You can get the smallest key:
>   - `data = {"a": 10, "c": 5, "b": 7}`
>   - `print(min(data))`   # "a"
> Or the smallest **value**:
>   - `print(min(data.values()))` # 5


> [!CAUTION]
> - **Iterable cannot be empty** → `min([])` gives an error.
> - **Types must be comparable** → numbers + strings = error.
> - **Strings use alphabetical order** → `"Ana"` < `"Maria"`.
> - **Use min(values) for dict values** → keys and values behave differently.
> - **min returns the value, not the index** → use `index()` if you need the position.



**Example:**
*Example 1 - Smallest number in a list*
`numbers = [5, 2, 9, 1]`
`print(min(numbers))`   # 1

*Example 2 - Smallest number in a tuple*
`values = (10, 3, 7)`
`print(min(values))`   # 3

*Example 3 - Smallest of multiple arguments*
`print(min(8, 4, 6))`   # 4


# 6 - Max()

## What it is:  
`max` is a **built‑in Python function** that returns the **largest value** in an iterable (list, tuple, set, etc.) or among multiple values.

>> “Give me the biggest element.”

> [!NOTE]
> ### Basic structure:
> **Using an iterable**
>    - `max(iterable)`
> **Using multiple values**
>    - `max(value1, value2, value3)`

> [!IMPORTANT]
> **## How `max` works**
> - With **numbers** → returns the highest number
> - With **strings** → returns the last alphabetically
> - With **mixed types** → ❌ error
> - With **empty iterables** → ❌ error


> [!TIP]
> **## Using `max` with dictionaries**
> Smallest key alphabetically:
>   - `data = {"a": 10, "c": 5, "b": 7}`
>   - `print(max(data))`   # "c"
> Largest **value**:
>   - `print(min(data.values()))` # 10


> [!CAUTION]
> - **Iterable cannot be empty** → `max([])` gives an error.
> - **Types must be comparable** → numbers + strings = error.
> - **Strings use alphabetical order** → `"Maria"` < `"Ana"`.
> - **Use max(values) for dict values** → keys and values behave differently.
> - **max returns the value, not the index** → use `index()` if you need the position.



**Example:**
*Example 1 - Largest number in a list*
`numbers = [5, 2, 9, 1]`
`print(max(numbers))`   # 9

*Example 2 - Largest number in a tuple*
`values = (10, 3, 7)`
`print(max(values))`   # 10

*Example 3 - Smallest of multiple arguments*
`print(max(8, 4, 6))`   # 8


# 7 - Len

## What it is:
`len` is a **built in Python function** that returns the **number of items** in a collection.

>> “Tell me how many elements this object has.”

> [!NOTE]
> ### You can use `len` with:
> 1. lists
> 2. strings
> 3. tuples
> 4. dictionaries
> 5. sets

> [!CAUTION]
> - **len works only on collections** → numbers like `10` or ´ don’t have length.
> - **Strings count characters** → including spaces.
> - **Dictionaries count keys** → not values.
> - **Nested lists count only top level** → `len([[1,2],[3,4]])` is 2.
> - **len returns an integer** → you can use it in comparisons.

> [!TIP]
> **## How `len` works**
> `len(object)` returns an **integer** representing how many elements the object contains.
> - **If the object is empty:**
> `print(len([]))`      # 0
> `print(len(""))`      # 0
> `print(len({}))`      # 0

> **Example:**
*Example 1 - Length of a list*
`fruits = ["apple", "banana", "orange"]`
`print(len(fruits))`   # 3

*Example 2 - Length of a string*
`text = "Python"`
`print(len(text))`   # 6

*Example 3 - Length of a dictionary (counts keys)*
`person = {"name": "Ana", "age": 25}`
`print(len(person))`   # 2




# 8 - Key

## What it is:
In Python, **key** is a term used mainly in **dictionaries**.

A **key** is:
>> “The name/identifier used to access a value inside a dictionary.”
A dictionary is made of **key–value pairs**:
     - `{"key": value}`


> [!NOTE]
> ### What a **key** does:
> A **key**:
> - identifies a value
> - must be **unique**
> - must be **immutable** (string, number, tuple…)
> - is used to **access**, **change**, or **remove values**


> [!IMPORTANT]
> ### Keys must be immutable:
> | **Valid keys** | **Invalid Keys** |
> | :--- | :--- |
> | strings | 	lists |
> | integeres | 	disctionaries |
> | floats | 	sets |
> | tuples | 	**Example:** `data = {[1, 2]: "test"}`   # ❌ error  |


> [!CAUTION]
> - **Keys must be unique** → duplicates overwrite.
> - **Keys must be immutable** → lists cannot be keys.
> - **Accessing a missing key gives error** → use `get()` to avoid it.
> - **Order is preserved in modern Python** → but keys still must be unique.
> - **Keys are used to loop through dictionaries** → default loop gives keys.

> [!WARNING]
> **## This is **not** allowed:**
> `data = {`
>     `"a": 1,`
>     `"a": 2`
> `}`
> Python keeps only the last `"a"`.



> **Example:**
*Example 1 - Dictionary with keys*
`person = {`
    `"name": "Ana",`
    `"age": 25,`
    `"city": "Porto"`
`}`

Here:
> - `"name"` is a **key**
> - `"age"` is a **key**
> - `"city"` is a **key**

*Example 2 - Accessing a value using a key*
`print(person["name"])`   # Ana

*Example 3 - Changing a value using a key*
`person["age"] = 30`

*Example 4 - Adding a new key*
`person["job"] = "Engineer"`

*Example 5 - Removing a key*
`person.pop("city")`

# Keys vs Values

| **Concept** | **Meaning** |
| :--- | :--- |
| **Key** | 	The identifier (e.g., `"name"`) |
| **value** | 	The data stored (e.g., `"Ana"`) |


# 9 - key=len

## What it is:
`key=len` is used in functions like **sorted()**, **min()**, **max()**, etc., to tell Python:

>> *“Use the length of each item as the criterion for comparison.”*

Ou seja:
 - **key** → diz qual função usar para comparar
 - **len** → é a função usada para medir cada item
Então **key=len** significa:
>> *“Compare items by their length.”*


> [!NOTE]
> ### Where you use key=len:
> Principalmente em:
> - **sorted**
> - **min**
> - **max**
> 

> [!TIP]
> ### How key=len works internally:
> Python does **not** compare the items directly.
> Instead, it does this:
> 1. Applies len() to each item
> 2. Uses the result to compare
> 
> **Exemplo:**
> `"apple"  → len = 5`  
> `"kiwi"   → len = 4`  
> `"banana" → len = 6`
> - **Depois ordena pelos números: 4, 5, 6.**


> [!IMPORTANT]
> ### Why key=len is useful:
> - Sorts by size instead of alphabet
> - Finds shortest/longest items
> - Works with strings, lists, tuples, etc.
> - Makes sorting more flexible and powerful


> [!CAUTION]
> - **Items must support len()** → numbers don’t work.
> - **Sorting is stable** → items with same length keep original order.
> - **key does not change the items** → only how they are compared.
> - **Works only in functions that accept key** → like sorted, min, max.



> **Example:**
*Example 1 - Sort strings by length*
`words = ["Python", "is", "amazing"]`
`print(sorted(words, key=len))`

**Output:**
> ['is', 'Python', 'amazing']
- Python sorted them by **length**, not alphabetically.

*Example 2 - Find the shortest word*
`words = ["apple", "banana", "kiwi"]`
`print(min(words, key=len))`   # kiwi

*Example 3 - Find the longest word*
`person["age"] = 30``words = ["apple", "banana", "kiwi"]`
`print(max(words, key=len))`   # banana

*Example 4 - Sort a list of lists by length*
`data = [[1, 2], [1], [1, 2, 3]]`
`print(sorted(data, key=len))`

*Example 5 - Removing a key*
`person.pop("city")`

**Output:**
> [[1], [1, 2], [1, 2, 3]]