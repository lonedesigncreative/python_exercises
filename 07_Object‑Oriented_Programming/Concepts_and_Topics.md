## 📘 What This Worksheet Introduces (Classes, Objects & Inheritance)

This worksheet introduces the foundations of **Object‑Oriented Programming (OOP)** in Python, focusing on how to create classes, instantiate objects, define methods, and apply inheritance.

---

### 🔹 Core Concepts — Classes & Objects
- **What a class is**  
  A blueprint that defines attributes (data) and methods (behaviors).

- **Creating a class**
  - Class name starts with a capital letter  
  - Defined using `class ClassName:`  

- **Constructor (`__init__`)**
  - Initializes object attributes  
  - Receives parameters to build each object  
  - Uses `self` to access instance variables  

- **Instance Variables**
  - Unique to each object  
  - Defined inside `__init__`  
  - Example: `self.ID`, `self.Nome`, `self.Idade`

- **Methods**
  - Functions inside a class  
  - Define object behavior  
  - Example: displaying data, validating age  

---

### 🔹 Core Concepts — Using Classes
- Creating objects (instances)  
  `pessoa1 = Pessoa(1, "Ana", 25)`
- Accessing methods  
  `pessoa1.MostraDadosPessoa()`
- Understanding how objects store and share data

---

### 🔹 Core Concepts — Importing Classes
- Classes can be stored in separate files  
- Imported using:  
  `from Pessoa import Pessoa`
- Allows modular and organized code

---

### 🔹 Core Concepts — Inheritance (OOP)
- **Single inheritance**  
  A subclass inherits attributes and methods from a superclass.
- Using `super()` to call the parent constructor  
- Extending behavior by adding new attributes and methods  
- Example hierarchy:
  - Superclass: `Pessoa`
  - Subclasses: `Aluno`, `Professor`

---

### 🔹 Practical Applications in the Exercises
- Creating classes for:
  - People  
  - Animals  
  - Products  
  - Books  
  - Software  
  - Coffee types  
  - Desserts  

- Each class includes:
  - Constructor with parameters  
  - Instance variables  
  - A method to display object data  
  - Creation of multiple objects  

- Applying inheritance to:
  - Extend the `Produto` class into `Livro` and `Software`  
  - Reuse parent attributes and methods  
  - Add subclass‑specific attributes  

---

### 🔹 Additional Skills Practiced
- Understanding how OOP models real‑world entities  
- Structuring code using classes and modules  
- Reusing code through inheritance  
- Combining constructors, methods, and object instances  
- Building more scalable and organized programs  

---

### ✅ Summary
This worksheet introduces the essential principles of **Object‑Oriented Programming in Python**: creating classes, defining constructors, building objects, writing methods, importing class files, and implementing inheritance. These concepts form the foundation for building structured, reusable, and professional‑grade Python applications.