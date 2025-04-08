import os
"""new_file = open("document.txt" , "x")
print(new_file)
new_file.close()"""


print("Checking if my_file exists or not ")
if os.path.exists("document.txt"):
    os.remove("document.txt")
else:
    print("The file does not exists ")

with open("document.txt" , "w") as file:
    file.write("Hello ! my name is Bunny and my age is 14 yrs.")
file.close()

os.remove("document.txt")

print("Checking the file exists or not ")
if os.path.exists("document.txt"):
    os.remove("document.txt")
else:
    print("The file does not exists")

#os.rmdir("lesson14")