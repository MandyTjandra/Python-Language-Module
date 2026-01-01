# Module 4: Arrays in Python

This module explains how to work with **Arrays**. Python does not have built-in support for Arrays, so we typically use **Python Lists** instead. For advanced scientific computing and faster performance, we use the **NumPy** library.

---

## 1. Python Lists as Arrays (`Array.py`)

Since Python lists can store multiple items in a single variable, they function just like arrays in other languages. You can access elements using their **index** (position), starting from 0.


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

1. **`Num[0]`**: Accesses the first element.
2. **`Num[0] = 10`**: Replaces the value at index 0 with 10.
3. **`len(Num)`**: Returns the total number of elements in the list.

### Iterating Through an Array

You can loop through an array directly or by using its index range.

```python
# 1. Loop by value
for num in Num: 
    print(num)

# 2. Loop by index (to print on one line)
for i in range(len(Num)): 
    if i < len(Num) - 1:
        print(Num[i], end=", ")
    else:
        print(Num[i])

```

---

## 2. Array Methods (`Array_Syntax.py`)

Python provides built-in methods to add, remove, and manipulate elements in a list.

```python
angka = [1, 2, 3, 4, 5]
print(angka) 

# Add element to the end
angka.append(6) 
print(angka) 

# Remove element at specific INDEX (index 2 is the number 3)
angka.pop(2) 
print(angka) 

# Remove specific VALUE (removes the number 1)
angka.remove(1) 
print(angka) 

```

**💡 Common Methods Cheat Sheet:**

* **`append()`**: Adds an element at the end.
* **`pop()`**: Removes an element at a specific position (index).
* **`remove()`**: Removes the first item with the specified value.
* **`sort()`**: Sorts the list alphabetically or numerically.
* **`reverse()`**: Reverses the order of the list.
* **`clear()`**: Removes all elements.

---

## 3. NumPy Arrays (`Numpy.py`)

For heavy mathematical computations, standard lists are too slow. **NumPy** (Numerical Python) is a library used for working with arrays efficiently.

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

1. **Performance**: Faster for large datasets compared to lists.
2. **Math**: Has built-in functions for complex computations (like Matrix algebra).
3. **Science**: Essential for Machine Learning and Data Analysis.
