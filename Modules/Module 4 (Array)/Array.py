# Python does not have built-in support for Arrays, 
# but Python Lists can be used instead. 
# However, to work with arrays in Python you will 
# have to import a library, like the NumPy library.

Num = [1, 2, 3]
x = Num[0]
y = Num[1]
z = Num[2]

print(Num) # Print whole array
print(x)
print(y + z)

Num[0] = 10 # Modify array value
x = Num[0]

print(Num)
print(x)

lenght = len(Num) # Length of array

print(lenght)

for num in Num: # Print value of array one by one
    print(num)

for i in range(len(Num)): # Print the value but in one line
    if i < len(Num) - 1:
        print(Num[i], end=", ")
    else:
        print(Num[i])