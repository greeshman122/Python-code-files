largestnumber = int(input("Enter the largest number : "))
smallestnumber = int(input("Enter the smallest number : "))

while(smallestnumber):
    numberStore = smallestnumber
    smallestnumber = largestnumber % smallestnumber
    largestnumber = numberStore

print("HCF is : " , largestnumber)