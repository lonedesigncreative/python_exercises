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


# 3 - +=

## What it is:
`+=` is an **augmented assignment operator** in Python.

>> “Add something to the variable and **update** the variable with the new value.”

> [!NOTE]
> ## It is the same as:
> `x = x + value`
> 
> But shorter and cleaner:
> `x += value`


> [!IMPORTANT]
> ### Why `+=` is useful:
> - Makes code shorter
> - Easier to read
> - Common in loops
> - Works with numbers, strings, lists
> - 
> **Example in a loop:**
> `total = 0`
> `for i in range(5):`
>     `total += i`

> [!CAUTION]
> - **Type must match** → you cannot do `"text" += 5`
> - **Lists use += to extend**, not to append a single item
> - **+= modifies the variable** (important with lists)

> **Example:**
*Example 1 - With numbers*
`x = 5`
`x += 3`
`print(x)`   # 8

> **Meaning:**
> - take the current value of x
> - add 3
> - store the result back in x

*Example 2 - With strings (concatenation)*
`text = "Hello"`
`text += " World"`
`print(text)`   # Hello World

*Example 3 - With lists (extend)*
`numbers = [1, 2]`
`numbers += [3, 4]`
`print(numbers)`   # [1, 2, 3, 4]

# Summary

| **Operator** | **Meaning** | **Example** |
| :--- | :--- | :--- |
| += | Add and update | `x += 1` |
| -= | Subtract and update | `x -= 1` |
| *= | Multiply and update | `x *= 2` |
| /= | Multiply and update | `x /= 2` |


# 4 - `If`

## What it is:  
An **if** statement checks a condition.
If the condition is **true**, the code inside **runs**.
If the condition is **false**, Python **skips it**.

> [!CAUTION]
> - **Indentation is required** → the code inside the `if` must be indented.
> - **If without else does nothing when false** → the program continues normally.
> - **Condition must be valid** → avoid writing text or invalid expressions inside the `if`.
> - **B****e careful with spacing** → `if age >= 18`: works, but `ifage>=18`: is invalid.

**Example:**
`score = 90`
`if score >= 80:`
   `print("Great job")`


# 5 - For (loop)
A **for loop** is used when you want to **repeat a block of code a specific number of times** or **go through each item in a sequence** (like a list, string, or range).

## What it means:
> “For each value in this sequence, do this action.”

> [!CAUTION]
> - **Indentation is required** → everything inside the loop must be indented.
> - **range upper limit is not included** → `range(1, 5)` stops at 4, not 5.
> - **Variable name is temporary** → `i`, `n`, `item` are just loop variables.
> - **Avoid infinite loops** → `for` loops normally don’t go infinite, but wrong ranges can cause issues.
> - **Be careful with input()** → convert values before using them in a range.
> - **Don’t modify the list while looping** → it can break the loop.

**Example:**
*1. Loop from 1 to 5*
`for i in range(1, 6):`
    `print(i)`

*2. Loop through a list*
`fruits = ["apple", "banana", "orange"]`

`for fruit in fruits:`
    `print(fruit)`

*3. Loop through each letter in a string*
`for letter in "Python":`
    `print(letter)`

*4. Sum numbers from 1 to 10*
`total = 0`

`for n in range(1, 11):`
    `total += n`

`print(total)`

> [!IMPORTANT]
> - #### How the `range()` works:
> The function **range** creates a sequence of numbers.
>   - `range(5)` → 0,1,2,3,4
>   - `range(1, 5)` → 1,2,3,4
>   - `range(1, 10, 2)` → 1,3,5,7,9 (step of 2)



# 6 - def

## What it is:  
`def` is a Python keyword used to define a function.

>> “Create a reusable block of code with a name.”

A function lets you:
- organize code
- avoid repetition
- receive inputs
- return outputs

> [!NOTE]
> ### Basic structure:
>    - `def function_name(parameters):`
>    - `code_block`
> **Example:**
>    - `def greet():`
>      - `print("Hello!")`


> [!IMPORTANT]
> **## What def does**
> - Creates a function
> - Gives it a name
> - Defines parameters
> - Defines the code that runs when the function is called

> [!TIP]
> **## Why functions are useful**
> - Avoid repeating code
> - Make programs easier to read
> - Allow modular programming
> - Allow reuse in different parts of the program

> [!CAUTION]
> - **Indentation is required** → code inside the function must be indented.
> - **Functions must be called** → defining is not enough.
> - **Return ends the function** → anything after return is ignored.
> - **Parameters must match** → wrong number of arguments gives error.
> - **Functions create their own scope** → variables inside are local.

**Example:**
*Example 1 - Function with no parameters*
`def say_hello():`
  `print("Hello, John!")`

Call it:
> say_hello()

*Example 2 - Function with one parameter*
`def greet(name):`
  `print("Hello", name)`

Call it:
> greet("Ana")


# 7 - return

## What it is:  
`return` is a keyword used inside a function in Python.

>> “Send a value back to the place where the function was called.”

When Python reaches a `return`, the function stops immediately and gives back a result.

> [!NOTE]
> ### Basic usage:
>    - `def function_name():`
>     - `return value`

> [!IMPORTANT]
> **## **Important: `return` ends the function****
>
> Anything after `return` is **ignored**.
>
> `def test():`
>     `return 10`
>     `print("This will NOT run")`

## `return` vs `print`

| **Concept** | **What it does** |
| :--- | :--- |
| return | Sends a value back to the caller |
| print | Shows text on the screen |

### **Example:**
`def f():`
    `return 5`

`print(f())`   # prints 5

> [!NOTE]
> `return` gives the value.
> `print` only displays it.

> [!TIP]
> ### Functions can return any type:
>
>   - **Number**
>     - `def get_number():`
>       - `return 42`
>
> 
> 
>   - **String**
>     - `def greet():`
>       - `return "Hello"`
>
> 
> 
>   - **List**
>     - `def numbers():`
>       - `return [1, 2, 3]`
>
>
> 
>   - **Boolean**
>     - `def is_adult(age):`
>       - `return age >= 18`
>
>**------------------------------------**
>
> ### Functions can return multiple values (as a tuple):
>
> `def stats(a, b):`
>     `return a + b, a * b`
>
> `s, m = stats(3, 4)`
> `print(s, m)`   # 7 12
>
> 
>
>  ### return without a value:
>
> `def empty():`
>     `return`
>
> - This returns `**None**`.
>
> **------------------------------------**
>
> ### If a function has no return
>
> Python automatically returns **None**.
>
> `def hello():`
>   `print("Hi")`
> 
> `x = hello()`
> `print(x)`   # None

# Summary

| **Feature** | **Meaning** |
| :--- | :--- |
| return | Sends a value back |
| Ends the function | Code after return is ignored |
| Can return any type | numbers, strings, lists, booleans |
| No return → None | default behavior |


# 8 - in

## What it is:  
O operador `in` verifica se **um valor existe dentro de outro valor**.

Em outras palavras:
>> “Está contido?”
>> “Pertence?”

Ele funciona com:
- **strings**
- **listas**
- **tuplas**
- **dicionários (chaves)**


> [!NOTE]
> ### Basic meaning:
>    - `if item in collection:`
>
> *True* se o item **estiver dentro** da coleção.
> *False* se **não estiver**.


> [!IMPORTANT]
> **## Truth table**
> 
> | **Expression** | **Result** |
> | :--- | :--- |
> | "a" in "cat" | True |
> | "z" in "cat" | False |
> | 3 in [1,2,3] | True |
> | "age" in {"age": 20} | True |
> | 20 in {"age": 20} | False |


> [!CAUTION]
>
> ## Common mistakes:
> 
> - `in` **em dicionários verifica chaves, não valores**
>   - ❌ `20 in {"age": 20}` → False
>   - ✔ `20 in person.values()` → True
> 
> - **Comparações incorretas**  
>   - ❌ `if "a" in "A"` → False (case sensitive)
> 
> - **Espaços contam**  
>   - `"hi" in "hi there"` → True
>   - `"hi " in "hi there"` → False


> [!TIP]
>
> ## Why `in` is useful
>
> - Verificar se um valor existe
> - Procurar texto dentro de texto
> - Validar opções
> - Verificar permissões
> - Verificar chaves em dicionários
>
> ### Practical examples:
>
> - **Checking user input**
> `answer = input("Continue? ")`
> 
> `if answer.lower() in ["yes", "y"]:`
>     `print("Continuing...")`
>
> - **Checking substring**
> `email = "example@example.com"`
> 
> `if "@" in email:`
>     `print("Valid email format")`


> **Example:**
*Example 1 - `in` with strings*
`word = "python"`

`if "py" in word:`
    `print("Found!")`

-  `"py"` está dentro de `"python"` → ***True***

*Example 2 - `i`n with lists*
`colors = ["red", "blue", "green"]`

`if "blue" in colors:`
    `print("Blue is here!")`

- `"blue"` está na lista.

*Example 3 - `in` with tuples*
`nums = (1, 2, 3)`

`if 2 in nums:`
    `print("2 is inside")`


*Example 4 - `in` with dictionaries*
`colors = ["red", "blue", "green"]`

`if "blue" in colors:`
    `print("Blue is here!")`


> [!WARNING]
> - `in` verifica **chaves**, não valores.


# Summary

| **Concept** | **Meaning** |
| :--- | :--- |
| in | Checks if a value exists inside another |
| Works with strings | `"a" in "cat"` |
| Works with lists | `3 in [1,2,3]` |
| Works with dictionaries | 	Checks keys |
| Case sensitive | `"A" in "a"` → False |