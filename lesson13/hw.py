# Opening a file in different access modes and performing operations

# 1. Create or overwrite a file and write data to it
with open('example.txt', 'w') as file:
    file.write("This is the initial content.\n")

# 2. Append new data to the file
with open('example.txt', 'a') as file:
    file.write("Adding new content in append mode.\n")

# 3. Read the entire content of the file
with open('example.txt', 'r') as file:
    print("Reading content:")
    print(file.read())

# 4. Read and write mode: Modify the content
with open('example.txt', 'r+') as file:
    content = file.read()
    file.seek(0)  # Move the cursor to the beginning
    file.write("Modified content at the beginning.\n" + content)

# 5. Verify the changes
with open('example.txt', 'r') as file:
    print("Updated content:")
    print(file.read())
