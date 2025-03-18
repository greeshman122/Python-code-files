class Person:
    def __init__(self , name , idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("The name of the person is " , self.name)
        print("The idnumber of the person is " , self.idnumber)
class employee(Person):
    def __init__(self , name , idnumber , salary , post):
        self.salary = salary
        self.post = post
        Person.__init__(self , name , idnumber)
E1 = employee(" Nagesh " , 814227474 , 50000 , "Developer")
E1.display()