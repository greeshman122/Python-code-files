cause = input("Do you have a medical cause ? Enter your answer as Yes and NO : ")
if cause == "Yes" :
    print("Allowed")
else:
    attendance=int(input("Enter your attendance percentage"))
    if attendance > 75:
        print("Allowed")
    else:
        print("Not Allowed")