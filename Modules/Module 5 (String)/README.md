# Module 5: Strings in Python

This module covers **Strings**, which are sequences of characters used to store text. In Python, strings are versatile: they can be treated like arrays, sliced, looped through, and formatted dynamically.

---

## 1. Creating Strings (`AssignString.py`, `Quotes_Inside_Quotes.py`, `Multilines.py`)

Strings can be created using single (`'`) or double (`"`) quotes.

```python
# 1. Basic Assignment
a = 'Hello'
print(a)

# 2. Quotes inside Quotes
# Use different quote types to nest them
print("It's alright")
print("He is called 'Johnny'")

# 3. Multiline Strings
# Use three quotes (""") for strings that span multiple lines
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit"""
print(a)

```

---

## 2. Strings as Arrays (`StringInArray.py`, `Slicing.py`, `LoopingString.py`)

Strings in Python are arrays of bytes representing Unicode characters. You can access individual characters using square brackets `[]`.

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

```

### Looping and Length

You can loop through the characters in a string or check its length.

```python
# Loop through letters
for x in "banana":
    print(x)

# Get string length
a = "Hello, World!"
print(len(a))     # Returns 13

```

---

## 3. Checking Strings (`CheckString.py`, `Not_in_String.py`)

You can check if a certain phrase or character is present in a string using the keywords `in` or `not in`.

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

Python has a set of built-in methods that you can use on strings. Note that strings are immutable, so these methods return a **new** string.

### Changing Case

```python
a = "Hello, World!"
print(a.upper())        # "HELLO, WORLD!"
print(a.lower())        # "hello, world!"
print(a.swapcase())     # "hELLO, wORLD!" (Swaps case)
print(a.capitalize())   # "Hello, world!" (First char upper, rest lower)

```

### Cleaning and Splitting

```python
# strip(): Removes whitespace from beginning or end
a = "   Hello, World!   "
print(a.strip())        # "Hello, World!"

# replace(): Replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J")) # "Jello, World!"

# split(): Splits the string into a list based on a separator
print(a.split(","))     # ['Hello', ' World!']

```

---

## 5. F-Strings and Formatting (`F_String.py`)

**F-Strings** allow you to embed expressions inside string literals, using curly braces `{}`.

```python
age = 36
price = 59

# Basic F-String
txt = f"My name is John, I am {age}"

# Math Operations
txt = f"The price is {20 * 59} dollars"

# Formatting Modifiers (e.g., fixed point number)
txt = f"The price is {price:.2f} dollars" # Rounds to 2 decimal places

```

---

## 6. Escape Characters (`Escape.py`, `CarriageReturn.py`)

To insert characters that are illegal in a string, use an escape character `\`.

```python
# \" allows you to use double quotes inside a double-quoted string
txt = "We are the so-called \"Vikings\" from the north."

# Common Escapes:
# \n = New Line
# \t = Tab
# \\ = Backslash
print("Hello \nWorld! \n\tThis is Mandy")

```

### The Carriage Return (`\r`)

The `\r` escape character moves the cursor back to the start of the line, allowing you to overwrite text (useful for loading bars).

```python
import time
for i in range(10):
    print(f"\rCounting: {i}", end="", flush=True)
    time.sleep(1)

```
