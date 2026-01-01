# Module 2: Conditionals in Python

This module introduces decision-making in Python. You will learn how to execute different blocks of code based on specific conditions using **If-Else** statements and how to simulate **Switch-Case** logic using Dictionaries.

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
4. **Indentation**: Python relies on indentation (whitespace) to define the blocks of code inside the `if` statement.

---

## 2. Simulating Switch-Case (`SwitchCase.py`)

While many languages have a `switch` or `case` statement, Python often uses **Dictionaries** to map values efficiently. This is cleaner than writing many `if-elif` statements when checking a single variable against many possible values.

```python
x = input("Masukkan kode plat Anda: ").upper()  # Convert input to uppercase

# Dictionary to map codes to locations
plat_dict = {
    'B': "Bekasi",
    'A': "Banten",
    'D': "Banten",
    'E': "Cirebon"
}

# Get the corresponding location or a default message
print(plat_dict.get(x, "Kode tidak diketahui"))
# Dictionary.get(key, default_value)

```

**💡 Code Explanation:**

1. **`.upper()`**: Converts the user's input to uppercase (e.g., 'b' becomes 'B') so the program isn't case-sensitive.
2. **Dictionary (`plat_dict`)**: Acts as a lookup table where keys ('B', 'A') point to values ("Bekasi", "Banten").
3. **`.get(x, "...")`**: Tries to find `x` in the dictionary. If `x` exists, it returns the city name. If `x` does **not** exist, it returns the default value ("Kode tidak diketahui") instead of crashing.
