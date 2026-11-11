# Module 1: Introduction to Python

This module covers the basics of Python programming. You will learn the fundamental syntax, how to use variables and comments, the different data types available, and how to perform operations using arithmetic and logical operators.

---

## 🎯 Learning Objectives

By the end of this module, students and learners will be able to:
- Write and execute basic Python programs using `print()`.
- Use single-line comments (`#`) to document code effectively.
- Understand dynamic typing and declare variables for integers, floats, and strings.
- Recognize Python's core data types (`int`, `float`, `str`, `list`, `tuple`, `dict`, `set`, `bool`).
- Perform type casting between numbers and strings using `int()`, `float()`, and `str()`.
- Capture and process console input from users with `input()`.
- Apply arithmetic, logical, and membership operators to evaluate expressions.

---

## 1. Basic Syntax (`HelloWorld.py`)

Python uses a very simple syntax. The most basic command is `print()`, which displays text or numbers to the console.

```python
print("Hello World!")
```

**💡 Code Explanation:**

1. **`print(...)`**: A built-in function that sends the text inside the parentheses to the screen.
2. **Strings**: Text must be enclosed in quotes (`""` or `''`).

---

## 2. Comments and Variables (`Comments.py`)

**Comments** are lines ignored by the computer, used to explain code. **Variables** are containers for storing data values. In Python, you don't need to declare the type (like `int` or `float`) explicitly; Python figures it out automatically.

```python
# An integer assignment
age = 45

# A floating point
salary = 1456.8

# A string
name = "John"

print(age)
print(salary)
print(name)
```

**💡 Code Explanation:**

1. **`#`**: Any text following this symbol is a comment.
2. **`age = 45`**: Creates a variable named `age` and stores the integer `45` in it.

---

## 3. Data Types (`DataTypes.py`)

Python has several built-in data types to store different kinds of information, from simple numbers to complex groups of data.

```python
a = "Hello World"                  # string (text)
b = 50                             # integer (whole number)
c = 60.5                           # float (decimal number)
d = 3j                             # complex number
e = ["geeks", "for", "geeks"]      # list (ordered, changeable)
f = ("geeks", "for", "geeks")      # tuple (ordered, unchangeable)
g = {"name": "Suraj", "age": 24}   # dict (key:value pairs)
h = {"geeks", "for", "geeks"}      # set (unordered, no duplicates)
i = True                           # bool (True or False)
j = b"Geeks"                       # binary

print(a)
# ... prints other variables
```

**💡 Code Explanation:**

1. **`List` (`[]`)**: A collection that is ordered and changeable.
2. **`Tuple` (`()`)**: A collection that is ordered but **cannot** be changed (immutable).
3. **`Dict` (`{}`)**: Stores data values in `key:value` pairs (like a real dictionary).

---

## 4. Type Casting (`Casting.py`)

Sometimes you need to convert one data type to another. This is called **Casting**.

```python
x = int(3.2)     # Will be 3 because integers can't have decimals
y = str("Halo!") # str = string
z = float(5.5)   # Float can have decimals

print(x)
print(y)
print(z)
```

**💡 Code Explanation:**

1. **`int()`**: Converts a value into an integer (drops the decimal part).
2. **`str()`**: Converts a value into a text string.
3. **`float()`**: Converts a value into a floating-point number.

---

## 5. Input and Output (`Input_and_Output.py`)

To make programs interactive, we use `input()` to get data from the user.

```python
# Python program show input and Output
val = input("Enter your value: ") 
print(val)
```

**💡 Code Explanation:**

1. **`input("...")`**: Pauses the program and waits for the user to type something and press Enter. The text inside `()` is the prompt shown to the user.
2. **Return Value**: The data typed by the user is **always returned as a String**. To do math on it, cast it: `int(input(...))`.

---

## 6. Operators (`Operator.py`, `LogicalOperator.py`, `IdentityOperator.py`)

Operators perform operations on variables and values.

### Arithmetic Operators

Used for math. Note the special operators for **Power** (`**`) and **Floor Division** (`//`).

```python
a = 9
b = 4

add = a + b 
sub = a - b 
mul = a * b 
mod = a % b    # Modulus (remainder)
p = a ** b     # Power (a to the power of b)
f = a // b     # Floor Division (rounds down to nearest whole number)

print(p) # 9^4 = 6561
print(f) # 9 // 4 = 2
```

### Logical Operators

Used to combine conditional statements.

```python
a = True
b = False

print(a and b) # False (because both are not True)
print(a or b)  # True (because at least one is True)
print(not a)   # False (inverts boolean value)
```

### Membership Operators

Used to test if a sequence is present in an object.

```python
x = ["apple", "banana"]

print("banana" in x)
# returns True because "banana" is in the list
```

---

## ⚠️ Common Pitfalls & Tips

1. **`input()` Always Returns a String**:
   ```python
   # ❌ Bug: "10" + "5" becomes "105" (string concatenation)
   a = input("Enter number 1: ")
   b = input("Enter number 2: ")
   print(a + b)

   # ✅ Fix: Cast to int or float first
   a = int(input("Enter number 1: "))
   b = int(input("Enter number 2: "))
   print(a + b) # 15
   ```
2. **Division `/` vs Floor Division `//`**:
   - `7 / 2` results in a float `3.5`.
   - `7 // 2` truncates the decimal part and returns integer `3`.
3. **Assignment (`=`) vs Equality (`==`)**:
   - `=` assigns a value to a variable (`x = 5`).
   - `==` compares two values (`x == 5`).

---

## 🧪 Hands-On Practice Challenges

Test your understanding by writing scripts for the following:

- 🟢 **Challenge 1 (Greeting Program)**:
  Ask the user for their name and their year of birth. Calculate and print their age in years.
- 🟡 **Challenge 2 (Simple Tip & Bill Calculator)**:
  Ask the user for the total restaurant bill amount and the percentage tip they want to give (e.g. 10%, 15%). Calculate the tip amount and the final total bill.
- 🔴 **Challenge 3 (Temperature Converter)**:
  Prompt the user to enter a temperature in Celsius. Convert it to Fahrenheit using the formula: $F = (C \times 9/5) + 32$, and display the result.
