#Program to count number of lines in this file
#Opening a file
file = open('sample.txt', 'r')
Counter = 0

# Reading from file
Content = file.read()
# Splitting content into lines
#and dtoring then in a iist
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)