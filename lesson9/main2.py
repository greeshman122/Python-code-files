class student:
    grade = 9
    name =  'Greeshman'
    def __init__(self):
        print("This is a constructor method")
    def details(self):
        print(" My grade is : " , self.grade , " and my name is : " , self.name )
s1 = student()
s1.details()