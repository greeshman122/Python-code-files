# Open the file in read mode
file = open('sample.txt', 'r')
print("File in read mode")
print(file.read())
file.close()

# Open the file in write mode
file_write = open('sample.txt', 'w')
# Write in the file
file_write.write('File in write mode')
file_write.write('Hi! I am Penguin. I am 1 yr old.')
file_write.close()

# Open the file in append mode
file_append = open('sample.txt', 'a')
file_append.write('\nFile in append mode')
file_append.write('Hi! I am Penguin. I am 1 yr old.')
file_append.close()