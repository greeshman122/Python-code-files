#reading the entire file at once
with open('bignotes.txt', 'r') as file:
    content = file.read()
    print(content)

#reading a file line by line
with open('bignotes.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Using `strip()` to remove leading/trailing spaces.

#reading a file specific number of characters
with open('bignotes.txt', 'r') as file:
    chunk = file.read(10)  # Reads 10 characters.
    print(chunk)

#store lines in a list
with open('bignotes.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#reading a file using a while loop
with open('bignotes.txt', 'r') as file:
    while (line := file.readline()):  # Using the walrus operator (Python 3.8+).
        print(line.strip())