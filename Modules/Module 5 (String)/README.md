# Module 5: Strings in Python

This module covers **Strings**, which are sequences of characters used to store and manipulate text. In Python, strings are versatile: they can be treated like sequences, sliced, searched, and formatted dynamically.

---

## 🎯 Learning Objectives

By the end of this module, students and learners will be able to:
- Instantiate single-line, multi-line (`"""`), and quote-nested strings.
- Access characters via zero-based indexing and extract substrings using slice notation `[start:stop:step]`.
- Reverse strings effortlessly using negative slicing (`[::-1]`).
- Check string containment with `in` and `not in`.
- Sanitize and transform textual data using `.strip()`, `.replace()`, `.split()`, `.upper()`, and `.lower()`.
- Construct dynamic output messages with modern **F-Strings** (`f"{variable}"`) and precision modifiers.
- Use escape sequences (`\n`, `\t`, `\"`) and carriage returns (`\r`) for command-line UI effects.

---

## 📁 Subfolder Overview

This module is organized into detailed topic folders:
* [`Python String/`](./Python%20String) — Core declarations, quote handling, and length checks.
* [`Slicing String/`](./Slicing%20String) — Indexing and substring slicing.
* [`Modify String/`](./Modify%20String) — String manipulation methods.
* [`Format String/`](./Format%20String) — F-string interpolation and modifiers.
* [`Concanate String/`](./Concanate%20String) — Combining string expressions.
* [`Escape Character/`](./Escape%20Character) — Escape codes and terminal animations.

---

## 1. Creating Strings (`AssignString.py`, `Quotes_Inside_Quotes.py`, `Multilines.py`)

Strings can be enclosed in single (`'`) or double (`"`) quotes.

```python
# 1. Basic Assignment
a = 'Hello'
print(a)

# 2. Quotes inside Quotes
# Alternate quote delimiters to nest quotes without escape characters
print("It's alright")
print("He is called 'Johnny'")

# 3. Multiline Strings
# Use triple quotes (""" or ''') for multi-line blocks
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit"""
print(a)
```

---

## 2. Strings as Sequences (`StringInArray.py`, `Slicing.py`, `LoopingString.py`)

Strings in Python are sequences of Unicode characters. You can access individual characters using square brackets `[]`.

### Indexing and Slicing

```python
a = "Hello, World!"

# Accessing a single character (Index starts at 0)
print(a[1])       # Returns 'e'

# Slicing (Get a range of characters)
print(a[2:5])     # Returns 'llo' (from index 2 up to, but not including, 5)
print(a[:5])      # Returns 'Hello' (from start to index 5)
print(a[2:])      # Returns 'llo, World!' (from index 2 to end)

# Negative Indexing (Slice from the end)
print(a[-5:-2])   # Returns 'orl'

# Reversing a string
print(a[::-1])    # Returns '!dlroW ,olleH'
```

### Looping and Length

```python
# Loop through letters
for char in "banana":
    print(char)

# Get string length
a = "Hello, World!"
print(len(a))     # Returns 13
```

---

## 3. Checking Strings (`CheckString.py`, `Not_in_String.py`)

Check whether a substring exists within a string using `in` and `not in`:

```python
txt = "The best things in life are free!"

# Check presence
if "free" in txt:
    print("Yes, 'free' is present.")

# Check absence
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
```

---

## 4. Modifying Strings (Methods)

Strings in Python are **immutable** (they cannot be changed in-place). String methods always return a **new** string.

### Case Transformations
```python
a = "Hello, World!"
print(a.upper())        # "HELLO, WORLD!"
print(a.lower())        # "hello, world!"
print(a.swapcase())     # "hELLO, wORLD!"
print(a.capitalize())   # "Hello, world!"
```

### Whitespace Removal and Splitting
```python
# strip(): Removes leading and trailing whitespace
a = "   Hello, World!   "
print(a.strip())        # "Hello, World!"

# replace(): Replaces matching substrings
a = "Hello, World!"
print(a.replace("H", "J")) # "Jello, World!"

# split(): Splits a string into a list of strings by a delimiter
print(a.split(","))     # ['Hello', ' World!']
```

---

## 5. F-Strings and Formatting (`F_String.py`)

**F-Strings** (formatted string literals) allow you to embed variables and expressions directly inside curly braces `{}`:

```python
age = 36
price = 59.9984

# Basic F-String
txt = f"My name is John, I am {age}"

# Inline math
txt = f"The price is {20 * 59} dollars"

# Precision modifiers (format floating point numbers)
txt = f"The formatted price is ${price:.2f}" # Produces: $60.00
```

---

## 6. Escape Characters (`Escape.py`, `CarriageReturn.py`)

To insert characters with special syntactic meaning, prefix them with a backslash `\`:

```python
txt = "We are the so-called \"Vikings\" from the north."
print("Hello\nWorld!\n\tIndented text")
```

### Terminal Overwriting with Carriage Return (`\r`)
The `\r` character moves the cursor back to the start of the current console line without advancing to the next line:

```python
import time

for i in range(1, 6):
    print(f"\rDownloading item {i}/5...", end="", flush=True)
    time.sleep(0.5)
print("\nDone!")
```

---

## ⚠️ Common Pitfalls & Tips

1. **Strings are Immutable:**
   ```python
   # ❌ Mistake: expecting text to change in-place
   text = "python"
   text.upper()
   print(text) # Still prints "python"!

   # ✅ Solution: reassign the returned string
   text = text.upper()
   print(text) # "PYTHON"
   ```
2. **Quote Clashing in F-Strings:**
   Avoid using the same quotes inside `{}` as the outer f-string quotes.
   ```python
   # ✅ Good:
   user = {"name": "Alice"}
   print(f"User: {user['name']}")
   ```

---

## 🧪 Hands-On Practice Challenges

- 🟢 **Challenge 1 (Palindrome Tester)**:
  Prompt the user for a word. Check if it reads the same forward and backward (e.g. `"racecar"`, `"radar"`). Ignore casing by converting to `.lower()`.
- 🟡 **Challenge 2 (Email Domain Parser)**:
  Ask the user to enter their email address (e.g. `jane.doe@university.edu`). Use `.split()` to extract and display the username and the domain name separately.
- 🔴 **Challenge 3 (Formatted Receipt Generator)**:
  Given a list of items and prices:
  `items = [("Notebook", 2.5), ("Pencil", 0.75), ("Backpack", 34.99)]`
  Use f-strings to print an aligned receipt where item names are left-aligned (20 characters wide) and prices are right-aligned with 2 decimal places.
