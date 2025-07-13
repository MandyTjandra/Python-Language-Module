import time

for i in range(10):
    print(f"\rCounting: {i}", end="", flush=True)
    time.sleep(1)

# In Python, a carriage return can be represented by \r. 
# It moves the cursor back to the beginning of the current 
# line without advancing to the next line, allowing you to 
# overwrite the current line.