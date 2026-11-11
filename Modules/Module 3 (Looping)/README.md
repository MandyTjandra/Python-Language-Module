# Module 3: Looping in Python

This module introduces **Loops**, which allow you to repeat a block of code multiple times. You will learn about **For Loops** (iterating over sequences or fixed ranges) and **While Loops** (repeating as long as a condition remains true).

---

## 🎯 Learning Objectives

By the end of this module, students and learners will be able to:
- Construct `for` loops using the built-in `range()` function.
- Understand the 3-argument syntax of `range(start, stop, step)`.
- Implement `while` loops with state variables and explicit increment/decrement conditions.
- Prevent and diagnose infinite loops.
- Use loop control statements such as `break` and `continue`.

---

## 1. For Loops (`For.py`)

A `for` loop is used when you know in advance how many times you want to iterate or when iterating over a sequence (such as a list, string, or number range).

```python
x = 0

# Loop from 0 up to (but not including) 4
for x in range(0, 4):
    print("Hello World!", x)
```

**💡 Code Explanation:**

1. **`range(start, stop)`**: Generates a sequence of integers starting at `start` (0) and terminating right before `stop` (4). Thus, the sequence produces `0, 1, 2, 3`.
2. **`range(start, stop, step)`**: You can also supply a third argument to control the step size (e.g., `range(0, 10, 2)` produces even numbers: `0, 2, 4, 6, 8`).
3. **`x`**: Iteration variable that automatically receives each subsequent value in the sequence.

---

## 2. While Loops (`While.py`)

A `while` loop continues executing as long as its conditional check evaluates to `True`. You must manually update state variables inside the loop body to reach a termination condition.

```python
x = 0

while x < 4:
    print("Hello World!", x)        # Adds a space automatically
    print("Hello World!" + str(x))  # Concatenation (no space)
    x += 1                          # Increment x to avoid infinite loop
```

**💡 Code Explanation:**

1. **`while x < 4:`**: The condition is evaluated before each iteration. When `x` reaches `4`, the loop terminates.
2. **`x += 1`**: Shorthand for `x = x + 1`. Incrementing the counter is essential—omitting this causes the loop to run indefinitely!
3. **Print Formatting**:
   * `print(..., x)`: Passing multiple arguments separated by commas automatically inserts spaces.
   * `print(... + str(x))`: String concatenation requires casting the integer to a string first (`str(x)`).

---

## 3. Loop Control: `break` and `continue`

Python provides two essential control keywords:
* **`break`**: Immediately exits the loop entirely.
* **`continue`**: Skips the rest of the current iteration and jumps to the next cycle.

```python
for i in range(1, 10):
    if i == 5:
        continue # Skip printing 5
    if i == 8:
        break    # Stop the loop completely when reaching 8
    print(i, end=" ")
# Output: 1 2 3 4 6 7
```

---

## ⚠️ Common Pitfalls & Tips

1. **Off-by-One in `range()`**:
   Remember that `range(1, 5)` stops before 5: it yields `1, 2, 3, 4` (total 4 elements, not 5).
2. **Accidental Infinite Loops**:
   If a `while` loop never changes its test condition or increments the counter, it freezes the program. Press `Ctrl + C` in the terminal to interrupt an infinite loop.
3. **Modifying Loop Counters in `for` loops**:
   In Python, assigning to `x` inside `for x in range(...)` will **not** change the sequence progression for the next cycle. Use `while` if you need custom jumping.

---

## 🧪 Hands-On Practice Challenges

- 🟢 **Challenge 1 (Countdown to Blastoff)**:
  Use a `for` loop with negative step in `range()` to count down from 10 down to 1, then print `"🚀 Blastoff!"`.
- 🟡 **Challenge 2 (Sum of First N Numbers)**:
  Prompt the user for a positive integer $N$. Calculate the sum of all integers from 1 up to $N$ using a loop (e.g. if $N=5$, $1+2+3+4+5=15$).
- 🔴 **Challenge 3 (The Classic FizzBuzz)**:
  Iterate numbers from 1 to 50:
  * If divisible by 3, print `"Fizz"`.
  * If divisible by 5, print `"Buzz"`.
  * If divisible by both 3 and 5, print `"FizzBuzz"`.
  * Otherwise, print the number itself.
