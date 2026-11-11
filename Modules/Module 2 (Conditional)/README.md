# Module 2: Conditionals in Python

This module introduces decision-making in Python. You will learn how to execute different blocks of code based on specific conditions using **If-Else** statements and how to simulate **Switch-Case** logic using Dictionaries.

---

## 🎯 Learning Objectives

By the end of this module, students and learners will be able to:
- Control program flow using `if`, `elif`, and `else` statements.
- Understand the importance of Python's whitespace indentation for defining code blocks.
- Construct compound logical conditions using comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
- Emulate `switch-case` constructs idiomatically using Python dictionaries and `.get()`.
- Provide safe fallback values to prevent KeyError exceptions when handling dynamic inputs.

---

## 1. If-Elif-Else (`Conditionals.py`)

The most common way to make decisions in code is using the `if`, `elif` (else if), and `else` keywords. This allows the program to react differently depending on the input.

```python
x = input("Masukkan 1 angka biner: ")

if x == "1":
    print("True")
elif x == "0":
    print("False")
else:
    print("Tidak diketahui")
```

**💡 Code Explanation:**

1. **`if x == "1":`**: Checks if the input is exactly equal to the string "1". If yes, it runs the indented code below it.
2. **`elif`**: Short for "Else If". If the first condition was False, it checks this next condition.
3. **`else`**: Catches everything that didn't match the previous conditions (like a default fallback).
4. **Indentation**: Python relies on 4-space indentation (whitespace) to define code blocks inside conditional branches.

---

## 2. Simulating Switch-Case (`SwitchCase.py`)

While many languages have a dedicated `switch` or `case` statement, Python traditionally uses **Dictionaries** to map values efficiently. This is cleaner and faster than writing dozens of repetitive `if-elif` statements.

```python
x = input("Masukkan kode plat Anda: ").upper()  # Convert input to uppercase

# Dictionary to map codes to locations
plat_dict = {
    'B': "Bekasi",
    'A': "Banten",
    'D': "Bandung",
    'E': "Cirebon"
}

# Get the corresponding location or a default message
print(plat_dict.get(x, "Kode tidak diketahui"))
# Dictionary.get(key, default_value)
```

**💡 Code Explanation:**

1. **`.upper()`**: Converts the user's input to uppercase (e.g., `'b'` becomes `'B'`) to make lookup case-insensitive.
2. **Dictionary (`plat_dict`)**: Acts as a hash table where keys (`'B'`, `'A'`) map directly to values (`"Bekasi"`, `"Banten"`).
3. **`.get(x, default)`**: Safely looks up key `x`. If found, it returns the mapped value. If not found, it returns the provided default message without throwing a `KeyError`.

---

## ⚠️ Common Pitfalls & Tips

1. **Missing Colon (`:`):**
   Every `if`, `elif`, and `else` line must terminate with a colon.
   ```python
   # ❌ SyntaxError: expected ':'
   if score >= 60
       print("Passed")

   # ✅ Correct:
   if score >= 60:
       print("Passed")
   ```
2. **Inconsistent Indentation:**
   Never mix tabs and spaces. Always stick to 4 spaces per indentation level.
3. **Chained Comparisons:**
   Python allows elegant chained conditions:
   ```python
   # Instead of: if score >= 80 and score < 90:
   if 80 <= score < 90:
       print("Grade: B")
   ```

---

## 🧪 Hands-On Practice Challenges

- 🟢 **Challenge 1 (Even or Odd Checker)**:
  Write a script that prompts the user for an integer and prints whether the number is **Even** or **Odd** using the modulo operator (`%`).
- 🟡 **Challenge 2 (Academic Grading Scale)**:
  Prompt the user for a test score between 0 and 100. Print the grade based on:
  * 90–100: **A**
  * 80–89: **B**
  * 70–79: **C**
  * 60–69: **D**
  * Below 60: **F**
  * Values outside 0–100: Print `"Invalid Score!"`
- 🔴 **Challenge 3 (Dictionary Day Planner)**:
  Use a dictionary to map day names (Monday through Sunday) to a planned activity. If the user types a day not on the list, display `"Rest Day!"` using `.get()`.
