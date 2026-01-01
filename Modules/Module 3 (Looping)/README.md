# Module 3: Looping in Python

This module introduces **Loops**, which allow you to repeat a block of code multiple times. You will learn about **For Loops** (repeating a specific number of times) and **While Loops** (repeating as long as a condition is true).


---

## 1. For Loops (`For.py`)

A `for` loop is used when you know exactly how many times you want to loop. In Python, we often use the `range()` function to define this.

```python
x = 0

# Loop from 0 up to (but not including) 4
for x in range(0, 4):
    print("Hello World!", x)

```

**💡 Code Explanation:**

1. **`range(0, 4)`**: Generates a sequence of numbers starting from **0** and stopping **before** 4. So, it runs for 0, 1, 2, and 3.
2. **`x`**: This variable updates automatically with the current number in the sequence for every iteration of the loop.

---

## 2. While Loops (`While.py`)

A `while` loop runs as long as a specific condition remains `True`. You must manually update variables inside the loop to eventually stop it (otherwise, you get an infinite loop!).

```python
x = 0

while x < 4:
    print("Hello World!", x)        # Adds a space automatically
    print("Hello World!" + str(x))  # Concatenation (no space)
    x += 1                          # Increment x to avoid infinite loop

```

**💡 Code Explanation:**

1. **`while x < 4`**: The code block runs only if `x` is less than 4.
2. **`x += 1`**: This increases `x` by 1 after every print. Without this line, `x` would always be 0, and the loop would run forever.
3. **Formatting Output**:
* `print(..., x)`: A comma adds an automatic space between items.
* `print(... + str(x))`: The `+` operator joins strings directly without spaces. You must cast `x` to a string (`str(x)`) because Python cannot add text and numbers directly.
