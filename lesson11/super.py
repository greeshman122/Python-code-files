class Person:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print("My fullname is " , self.fname + self.lname)
class Student(Person):
    def __init__(self , fname , lname , year):
        self.year = year
        super().__init__(fname , lname)
s1 = Student("Greeshman" , " Guntoju" , 2019)
s1.print()