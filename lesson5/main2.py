def addition(x,y):
    return(x+y)
def subtraction(x,y):
    return(x-y)
def multiplication(x,y):
    return(x*y)
def division(x,y):
    return(x/y)

num1 = int(input("Enter you value"))
num2 = int(input("Enter you value"))

print("Sum is ", addition(num1,num2))
print("Difference is ", subtraction(num1,num2))
print("Product is ", multiplication(num1,num2))
print("Reminder is ", division(num1,num2))