import numpy as np

# Create a NumPy array
Num = np.array([10, 20, 30])

# Access elements
x = Num[0]
y = Num[1]
z = Num[2]

# Print the array
print("Array:", Num)

# Perform arithmetic operation
result = y + z
print("Sum of second and third elements:", result)

# Modify an element
Num[0] = 50
print("Modified array:", Num)

# Calculate the sum of all elements
total = np.sum(Num)
print("Total sum of elements:", total)

# NumPy is essential for tasks that involve:
# 1. Large datasets or high-performance requirements.
# 2. Complex mathematical computations.
# 3. Scientific and numerical computing.
# 4. Applications like machine learning, data analysis, and engineering simulations.