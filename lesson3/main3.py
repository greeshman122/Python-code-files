number = int(input("Enter number to check : "))
if number>50:
    print("Number is greater than 50")
    if number%2==0:
        print("And it is even ")
    else:
        print("And it is odd")
else:
    print("Number is less than 50")