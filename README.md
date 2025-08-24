# Assignment-4
# Task-1
# File Reading in Python

This project demonstrates how to **read lines from a text file** in Python while handling errors gracefully.

## Code Explanation

```python
try:
    file = open('sample.txt', 'r')         # Open file in read mode
    file1 = file.readline().strip()        # Read first line and remove trailing newline
    file2 = file.readline()                # Read second line (keeps newline)
    
    print('Reading file content: ')
    print('Line 1: ', file1)
    print('Line 2: ', file2)
    
    file.close()                           # Close file after reading

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
```
Key Features

File Handling: Reads specific lines from a text file.

.strip(): Removes unwanted trailing newline or spaces from the first line.

Error Handling: Uses try-except block to catch FileNotFoundError if the file does not exist.

OUTPUT
```
Reading file content: 
Line 1:  This is a sample text file.
Line 2:  It contains multiple lines.
```

# Task-2
# File Writing, Appending, and Reading in Python

This project demonstrates how to **write, append, and read text files** in Python.

## Code Explanation

```python
a = input("Enter text to write to the file: ")
file = open('output.txt', 'w')              # Open file in write mode (creates/overwrites file)
file1 = file.write(a + '\n')                # Write user input with newline
print('Data Successfully written to output.txt.\n')
file.close()

b = input("Enter additional text to append: ")
file = open('output.txt', 'a')              # Open file in append mode (adds text to the end)
file2 = file.write(b + '\n')                # Append new input with newline
print('Data Successfully appended.\n')
file.close()

print("Final content of output.txt: ")
file = open('output.txt', 'r')              # Open file in read mode
file1 = file.read()                         # Read entire content of the file
print(file1)
file.close()
```
Key Features

Write Mode ('w')
```
Creates a new file if it doesn’t exist.
Overwrites existing content.
```
Append Mode ('a')
```
Adds new content at the end without deleting previous data.
```
Read Mode ('r')
```
Reads and displays file content.
```
File Closing
```
Ensures the file is saved properly and prevents corruption.
```
output
<img width="936" height="328" alt="image" src="https://github.com/user-attachments/assets/96cae9a2-25bd-4d4a-8a82-5b8feb358533" />
