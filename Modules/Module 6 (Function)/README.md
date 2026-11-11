# Module 6: Functions and Classes in Python

This module covers two major building blocks of modular Python programming. First, we explore **Functions** to organize reusable logic and examine how Python handles object references in memory. Next, we dive into **Object-Oriented Programming (OOP)** to structure code using Classes and Objects.

---

## 🎯 Learning Objectives

By the end of this module, students and learners will be able to:
- Define and call modular functions using `def` and the `return` statement.
- Distinguish between function **parameters** (definitions) and **arguments** (calls).
- Accept variable numbers of positional arguments using `*args`.
- Understand object memory references and check identity with `id()` and memory size with `sys.getsizeof()`.
- Design custom classes as object blueprints.
- Initialize instance state using the `__init__()` constructor and the `self` keyword.
- Define object methods that interact with and mutate instance state.
- Implement the `__str__()` dunder method for clean, readable string representations.

---

## 📁 Subfolder Overview

* [`Function/`](./Function) — Defining functions, passing arguments, and returning computed values.
* [`Pointer/`](./Pointer) — Variable-length tuples (`*args`), memory references, and object sizes.
* [`Class/`](./Class) — Class syntax, constructors, methods, `self`, and `__str__`.

---

## Part 1: Functions

Functions allow you to wrap code into named blocks that can be executed repeatedly from anywhere in your program.

### 1. Basic Functions (`Function.py`)
Use the `def` keyword followed by the function name and parentheses:

```python
def printf():
    print("This is a function.")

printf() # Calling the function
```

### 2. Arguments and Parameters (`Argument.py` & `Math.py`)

* **Parameter**: The variable specified inside the parentheses in the function header.
* **Argument**: The actual value provided to the function when invoked.

```python
# 1. Single Parameter
def my_function(fname):
    print(fname + " Refsnes")

# 2. Multiple Parameters
def math(a, b):
    c = a + b
    print("Hasil pertambahannya adalah", c)

# Getting input for the function
a, b = map(int, input("Masukkan 2 angka: ").split())
math(a, b)
```

### 3. Arbitrary Arguments (`Pointer.py`)

If the number of arguments is variable or unknown in advance, prefix the parameter with `*`. The function collects all arguments into a **tuple**:

```python
def my_function(*kids):
    # Access items using index
    print("The youngest child is " + kids[2]) 
    return kids

kids_names = my_function("Emil", "Tobias", "Linus")
```

### 4. Memory and Object References (`PengenalanPointer.py`)

Unlike low-level languages like C/C++, Python manages memory automatically through reference counting and garbage collection. Variables are references to objects stored in memory.

```python
import sys

a = 10
ptr = a # 'ptr' references the exact same object in memory as 'a'

# Check Memory Address (unique ID of the object)
print(f"Alamat dari a (id): {id(a)}")

# Check Size in Bytes
print(f"Ukuran dari nilai a adalah {sys.getsizeof(a)} bytes")
```

---

## Part 2: Classes and Objects (OOP)

Classes act as blueprints for creating custom objects that bundle data attributes together with behavioral methods.

### 5. Creating a Class (`Class.py` & `Pass.py`)

```python
class MyClass:
    x = 5

p1 = MyClass() # Instantiate an Object
print(p1.x)    # Access Attribute (5)
```

If a class definition is empty (e.g. stubbing out design), use `pass` to maintain valid syntax:
```python
class PendingImplementation:
    pass
```

### 6. The `__init__` Constructor (`Init.py` & `Class2.py`)

The `__init__()` method runs automatically whenever a new instance of the class is created. It initializes instance variables:

```python
class Mahasiswa:
    def __init__(self, nama, nrp, umur):
        self.nama = nama
        self.nrp = nrp
        self.umur = umur

mhs1 = Mahasiswa("Ahmad", "05111940000012", 18)
print(f"Nama: {mhs1.nama}")
```

### 7. Object Methods & `self` (`ObjectMethod.py` & `SelfParameter.py`)

Methods are functions defined inside a class body. The first parameter is always `self`, which represents the specific instance invoking the method:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

### 8. String Representation (`str.py`)

The `__str__()` method defines how the object should be formatted when printed or converted with `str()`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1) # Output: John(36)
```

---

## ⚠️ Common Pitfalls & Tips

1. **Omitting `self` in Method Signatures:**
   ```python
   # ❌ TypeError: greet() takes 0 positional arguments but 1 was given
   class Bot:
       def greet():
           print("Hello!")

   # ✅ Correct:
   class Bot:
       def greet(self):
           print("Hello!")
   ```
2. **Forgetting the `return` statement:**
   If a function calculates a value but omits `return`, calling it evaluates to `None`.
3. **Avoid Mutable Default Arguments:**
   Never use mutable objects (like `def func(items=[])`) as default parameter values, because the same list is reused across calls. Use `items=None` instead.

---

## 🧪 Hands-On Practice Challenges

- 🟢 **Challenge 1 (Temperature Conversion Functions)**:
  Write two functions:
  * `celsius_to_fahrenheit(c)` which returns the converted temperature.
  * `fahrenheit_to_celsius(f)` which returns the reverse.
  Test both functions with sample values and print formatted results.
- 🟡 **Challenge 2 (Arbitrary Statistics Function)**:
  Write a function `calculate_stats(*numbers)` that takes any quantity of numbers and returns a dictionary with the count, sum, and average of the numbers.
- 🔴 **Challenge 3 (Bank Account Class)**:
  Design a `BankAccount` class with:
  * Attributes: `account_holder` (string) and `balance` (float, defaults to `0.0`).
  * Methods: `deposit(amount)`, `withdraw(amount)` (prevent overdrafts if amount exceeds balance!), and `__str__()` to display `"[Holder]: Balance = $X.XX"`.
