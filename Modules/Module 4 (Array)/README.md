# Module 4: Arrays and Lists in Python

This module explains how to work with ordered collections of data. Python provides **Lists** as its versatile native sequence type. For scientific computing and high-performance multi-dimensional arrays, we utilize the **NumPy** library.

---

## 🎯 Learning Objectives

By the end of this module, students and learners will be able to:
- Create, access, and modify elements in Python lists using zero-based indexing.
- Determine collection length using `len()`.
- Iterate through collections by value (`for item in list`) and by index (`for i in range(len(list))`).
- Manipulate lists using built-in methods (`.append()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`).
- Understand when and why to use **NumPy** for numerical computations and matrix operations.

---

## 1. Python Lists as Arrays (`Array.py`)

Since Python lists can store multiple items in a single variable, they function just like dynamic arrays in other programming languages. You access elements using their **index** (position), starting from `0`.

```python
# Python Lists can be used as Arrays
Num = [1, 2, 3]

# Accessing elements (Index starts at 0)
x = Num[0]      # 1
y = Num[1]      # 2
z = Num[2]      # 3

print(Num)      # Print whole array
print(x)
print(y + z)    # 2 + 3 = 5

# Modifying a value
Num[0] = 10     
print(Num)      # [10, 2, 3]

# Getting the length
lenght = len(Num) 
print(lenght)   # 3
```

**💡 Code Explanation:**

1. **`Num[0]`**: Accesses the first element in the list.
2. **`Num[0] = 10`**: Mutates the list in-place by assigning a new value to index 0.
3. **`len(Num)`**: Built-in function that returns the total count of elements.

### Iterating Through an Array

You can loop through an array directly by value or by using index ranges:

```python
# 1. Loop by value (cleanest and most Pythonic)
for num in Num: 
    print(num)

# 2. Loop by index (useful when position matters)
for i in range(len(Num)): 
    if i < len(Num) - 1:
        print(Num[i], end=", ")
    else:
        print(Num[i])
```

---

## 2. Array Methods (`Array_Syntax.py`)

Python provides powerful methods to mutate lists:

```python
angka = [1, 2, 3, 4, 5]
print(angka) 

# Add element to the end
angka.append(6) 
print(angka) 

# Remove element at specific INDEX (index 2 removes value 3)
angka.pop(2) 
print(angka) 

# Remove specific VALUE (removes the first occurrence of value 1)
angka.remove(1) 
print(angka) 
```

**💡 Common Methods Quick Reference:**

| Method | Description | Example |
| :--- | :--- | :--- |
| `.append(val)` | Appends `val` to the end of the list | `nums.append(10)` |
| `.insert(idx, val)` | Inserts `val` at index `idx` | `nums.insert(0, 99)` |
| `.pop(idx)` | Removes and returns the item at index `idx` (default last) | `last = nums.pop()` |
| `.remove(val)` | Removes the first occurrence of `val` | `nums.remove(42)` |
| `.sort()` | Sorts items in ascending order in-place | `nums.sort()` |
| `.reverse()` | Reverses the list elements in-place | `nums.reverse()` |
| `.clear()` | Removes all elements from the list | `nums.clear()` |

---

## 3. NumPy Arrays (`Numpy.py`)

When working with hundreds of thousands of numbers, standard Python lists consume significant memory overhead. **NumPy** (Numerical Python) provides dense, C-speed array structures.

```python
import numpy as np

# Create a NumPy array
Num = np.array([10, 20, 30])

# Access and Modify
print("Array:", Num)
Num[0] = 50
print("Modified array:", Num)

# Mathematical Operations
total = np.sum(Num)
print("Total sum of elements:", total)
```

**💡 Why use NumPy?**
1. **Performance**: Vectorized operations execute in compiled C code without Python loop overhead.
2. **Convenience**: Direct matrix arithmetic (e.g. `arr * 2` multiplies every element by 2).
3. **Standard**: Essential foundation for Pandas, SciPy, Matplotlib, and Machine Learning libraries.

---

## ⚠️ Common Pitfalls & Tips

1. **`IndexError: list index out of range`**:
   Trying to access `nums[len(nums)]` will fail because indexing ends at `len(nums) - 1`.
2. **`.pop()` vs `.remove()`**:
   - `list.pop(2)` removes by **index** (the item sitting at slot 2).
   - `list.remove(2)` removes by **value** (searches for the number 2).
3. **Reference vs Copy**:
   ```python
   # ⚠️ Warning: Both refer to the exact same list!
   list_a = [1, 2, 3]
   list_b = list_a
   list_b.append(4)
   print(list_a) # [1, 2, 3, 4]

   # ✅ To make an independent copy:
   list_c = list_a.copy() # or list_a[:]
   ```

---

## 🧪 Hands-On Practice Challenges

- 🟢 **Challenge 1 (Max, Min, and Average)**:
  Given a list of student test scores `scores = [78, 92, 65, 88, 70, 95]`, write code to calculate and display the highest score, lowest score, and class average without using built-in `max()` or `min()` functions.
- 🟡 **Challenge 2 (Unique Sorted Elements)**:
  Write a script that takes a list with duplicate numbers `[4, 1, 2, 4, 3, 2, 5, 1]`, removes all duplicates, sorts the remaining numbers in ascending order, and prints the result.
- 🔴 **Challenge 3 (NumPy Vectorized Calculation)**:
  Create a NumPy array with the temperatures in Celsius: `celsius = np.array([0, 15, 22, 30, 37, 100])`. Convert the whole array to Fahrenheit in a single vectorized formula ($F = C \times 1.8 + 32$) and print the resulting array.
