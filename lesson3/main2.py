weight = float(input("Enter your weight in kgs : "))
height = float(input("Enter your height in cms : "))
BMI = weight/(height/100)**2
print("Your BMI value is : " , BMI)
if BMI<18.5:
    print("You are underweight")
elif BMI>18.5 and BMI<=24.9:
    print("You are normal")
elif BMI>25 and BMI<=29.9:
    print("You are overweight")
elif BMI>30 and BMI<=34.9:
    print("You are obese")
else : 
    print("You are extremely obese")