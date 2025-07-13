a = 'Hello World'
print(a[2:5]) # Get characters from position 2 to 5 (index 4)

b = "Hello, World!"
print(b[:5]) # Slice from the start to position 5 (index 4)

b = "Hello, World!"
print(b[2:]) # Slice from position 2 to the end

b = "Hello, World!"
print(b[-5:-2]) # Use negative indexes to start the slice 
                # from the end of the string.
                # Example:
                # Get the characters:
                # From: "o" in "World!" (position -5)
                # To, but not included: "d" in "World!" (position -2):
