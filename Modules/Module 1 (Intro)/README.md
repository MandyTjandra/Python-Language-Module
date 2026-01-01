# Module 1: Introduction to Python

This module covers the basics of Python programming. You will learn the fundamental syntax, how to use variables and comments, the different data types available, and how to perform operations using arithmetic and logical operators.

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
2. **Return Value**: The data typed by the user is always returned as a **String**.

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

```

### Membership Operators

Used to test if a sequence is presented in an object.

```python
x = ["apple", "banana"]

print("banana" in x)
# returns True because "banana" is in the list

```
