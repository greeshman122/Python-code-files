#open file and read its contents
file = open("Codingal.txt", "r")
print(file.read())
file.close()

#open file and read its beginning 8 characters
file1 = open("Codingal.txt" , "r")
print(file1.read(8))
file1.close()

#append your name ang age in the file
file2 = open("Codingal.txt" , "a")
file2.write("Hi ! I am Greeshman  I am 14 years old")
file2.close()

#open the file in read mode
file_read = open("codingal.txt" , "r")
print("File in read mode - ")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open("codingal.txt" , "w")
#write in the file
file_write.write("File in write mode ....")
file_write.write("Hi ! I am Greeshman . I am 14 years . Old")
file_write.close()

#open the file in append mode
file_append = open("codingal.txt" , "a")
#append in the file
file_append.write("\n File in append mode...")
file_append.write("Hi ! I am Greeshman . I am 14 years old .")
file_append.close()

#program to remove lines starting with any prefix
file1 = open("codingal.txt" , "r")
file2 = open("codingal.txt" , "w")
#reading each line from original
#text file
for line in file1.readlines():
    #reading all lines that do not
    #begin with "Codingal"
    if not (lines.startswith('codingal')):
        #printing those lines
        print(line)
        #storing only those lines that
        #do not begin with "Codingal"
        file2.write(line)
#close and save the files
file2.close()
file1.close()

#program to copy odd lines of one file to another
#open file in read mode
fn = open("codingal.txt" , "r")

#open other file in write mode
fn1 = open("CodingalUpdated.txt" , "w")

#read the content of the file line by line
cont = fn.readlines()
type(cont)
for i in range(1 , len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass
#close the file
fn1.close()
#open file in read mode
fn1 = open("codingalUpdated.txt" , "r")
#read the content of the file
cont1 = fn1.read()
#print the content of the file
print(cont1)
#lose all files
fn.close()
fn1.close()