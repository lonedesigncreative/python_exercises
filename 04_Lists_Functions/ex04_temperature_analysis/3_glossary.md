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

# 3 - Division (`/`)

## What it does:  
Divides one value by another.
Always returns a decimal (float).

> [!CAUTION]
> - Division always returns a decimal (float).
> - Be careful with dividing by zero - it causes an error.

**Example:**
`result = 10 / 4   # 2.5`


# 4 - f-string (f"")

## What it is:
An f string is a special type of text that allows you to insert variables inside the text.

> [!CAUTION]
> - Don’t forget the **f** before the quotes.
> - Without the **f**, Python will not replace the variables.

You write it with the letter f before the quotes:
`f"Hello {name}"`


# 5 - { }
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


# 6 – import

## What it means:
The import statement is used to bring code from another module or library into your Python program.

>> Use functions, tools, or code that were created somewhere else.

> [!TIP]
> Python has many built in modules (like math, random, datetime) and you can also import your own files.

> [!CAUTION]
> - **Module name must exist** → if the file or library doesn’t exist, Python gives an error.
> - **Avoid name conflicts** → don’t use the same name for variables and modules.
> - **Use aliases to simplify** → like import numpy as np.
> - **Import only what you need** → keeps your code clean and faster.
> - **Your file must be in the same folder** → when importing your own modules.
> - **Do not overuse from module import *** → it can cause confusion.

**Example:**
***Example 1 - Import a whole module***
`import math`
`print(math.sqrt(25))`   # 5.0

***Example 2 - Import only one function***
`from math import sqrt`
`print(sqrt(16))`   # 4.0

***Example 3 - Import with an alias (nickname)***
`import random as r`
`print(r.randint(1, 10))`

***Example 4 - Import multiple functions***
`from math import sin, cos, pi`
`print(sin(pi/2))`   # 1.0

***Example 5 - Import your own file***
import utils # import utils


# 7 – as

## What it is:
In Python, the keyword as is used to create an alias — a nickname — for something you are importing.

>> “Use this shorter or easier name instead of the original one.”

> [!NOTE]
> It is often used for large modules or modules with long names.

> [!CAUTION]
> - **Choose clear aliases** → don’t use random letters that confuse the reader.
> - **Alias replaces the original name** → after using `as`, you must use the alias, not the original name.
> - **Avoid overwriting variables** → don’t use an alias that is already a variable in your code.
> - **Follow conventions** → e.g., `import numpy as np` is standard.

**Example:**
***Example 1 - Alias for a module***
`import math as m`
`print(m.sqrt(25))`   # 5.0

***Example 2 - Alias for a function***
`from math import sqrt as raiz`
`print(raiz(16))`   # 4.0

***Example 3 - Alias for a library (very common)***
`import pandas as pd`
`import numpy as np`

***Example 4 - Alias for a library (very common)***
`import utils as u`
`u.my_function()`

> [!IMPORTANT]
> # **Why use `as`?**

> - To make the code shorter
> - To make names easier to type
> - To avoid name conflicts
> - To follow common conventions (ex.: `pd`, `np`, `plt`)



# 8 - [ ]

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


# 9 - Len

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


# 10 - Sum

## What it is:  
`sum` is a **built in Python function** that adds **all the numbers in an iterable** (like a list, tuple, or set) and returns the **total**.

>> “Add all these values and give me the result.”

> [!NOTE]
> ### Basic structure:
>    - `sum(iterable)`
> **or**
>    - `sum(iterable, start_value)`

> [!TIP]
> **## Common uses**
> **Total of a list**
> **Sum of even/odd numbers**
> **Sum of values in a loop**
> **Sum of dictionary values** (using `.values()`)
> - **Example:**
>   - `scores = {"Ana": 10, "João": 15, "Maria": 20}`
>   - `print(sum(scores.values()))`   # 45

> [!CAUTION]
> - **Iterable must contain numbers** → otherwise it errors.
> - **Start value must be a number** → `sum(list, "a")` is invalid.
> - **Large lists are fine** → sum is optimized.
> - **Use sum, not manual loops** → cleaner and faster.
> - **Works only with iterables** → not with single numbers.

> [!WARNING]
> **## What break does NOT do**
> It **cannot** add strings
> It **cannot** add lists
> It **cannot** add mixed types (e.g., number + string)
>   - `sum(["a", "b"])   # ❌ error`

**Example:**
*Example 1 - Sum of a list of numbers*
`numbers = [1, 2, 3, 4]`
`print(sum(numbers))`   # 10

*Example 2 - Sum of a tuple*
`values = (10, 20, 30)`
`print(sum(values))`   # 60


# 11 - Min()

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


# 12 - Max()

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


# 13 - Mean()

## What it is:  
`mean` is a function used to calculate the average of a set of numbers.

>> “Add all the values and divide by how many values there are.”

In Python, `mean` is part of the **statistics** module.
> `from statistics import mean`


> [!NOTE]
> ### Basic structure:
>    - `mean(iterable)`


> [!IMPORTANT]
> **## How `mmean` works**
> **THE FORMULAS IS:**
>    - mean = sum of values / number of values
> **Example:**
>    - `mean([2, 4, 6]) = (2 + 4 + 6) / 3 = 4`


> [!TIP]
> **## Alternative without importing**
> You can calculate the mean manually:
>   - `numbers = [10, 20, 30]`
>   - `average = sum(numbers) / len(numbers)`
> 
>   - `print(average)`   # 20


> [!CAUTION]
> - **Import required** → `from statistics import mean`.
> - **Iterable must contain numbers** → no strings.
> - **Empty list gives error** → cannot divide by zero.
> - **Floating point results** → mean often returns decimals.
> - **Use sum/len as alternative** → when you don’t want to import.


> [!WARNING]
> **## What break does NOT do**
> It **cannot** calculate the mean of strings
> It **cannot** calculate the mean of mixed types
> It **cannot** calculate the mean of an empty list


**Example:**
*Example 1 - Mean of a list of numbers*
`from statistics import mean`

`numbers = [10, 20, 30]`
`print(mean(numbers))`   # 20

*Example 2 - Mean of a tuple*
`values = (10, 3, 7)`
`print(mean(values))`   # 7

*Example 3 - Mean of a large list*
`scores = [12, 15, 18, 20, 25]`
`print(mean(scores))`   # 18


# 14 - Statisctics

## What it is:  
`statistics` is a Python module that provides functions for basic statistical calculations.

>> “A toolbox with functions to calculate averages, medians, variances, standard deviations, etc.”

To use it, you must import it:
> `import statistics`
Or import specific functions:
> `from statistics import mean, median`


> [!NOTE]
> ### What the statistics module can do:
> Here are the most common functions:
>   - **mean** → average
>   - **median** → middle value
>   - **mode** → most frequent value
>   - **stdev** → standard deviation
>   - **variance** → how spread out the data is
>   - **median_low** → lower median
>   - **median_high** → upper median
>   - **median_grouped** → median for grouped data


> [!IMPORTANT]
> **## How `mmean` works**
> **THE FORMULAS IS:**
>    - mean = sum of values / number of values
> **Example:**
>    - `mean([2, 4, 6]) = (2 + 4 + 6) / 3 = 4`


> [!TIP]
> - It is **built into Python** (no installation needed)
> - It is **simple and accurate**
> - It avoids writing formulas manually
> - It is perfect for **data analysis**, **school exercises**, **Power BI logic**, and **Python learning**


> [!CAUTION]
> - **Lists cannot be empty** → many functions need at least 1 or 2 values.
> - **Data must be numeric** → no strings.
> - **Mode can fail if no unique mode** → raises an error.
> - **stdev and variance need 2+ values** → cannot calculate with one number.
> - **Import required** → functions are not built‑in.



**Example:**
*Example 1 - Mean (average)*
`from statistics import mean`
`print(median([1, 3, 5]))`   # 20

*Example 2 - Median*
`from statistics import median`
`print(mean(values))`   # 3

*Example 3 - Mode*
`from statistics import mode`
`print(mode([2, 2, 3, 4]))`   # 2

*Example 2 - Standard deviation*
`from statistics import stdev`
`print(stdev([10, 12, 23, 23, 16])) `

*Example 3 - Variance*
`from statistics import variance`
`print(variance([10, 12, 23, 23, 16]))`