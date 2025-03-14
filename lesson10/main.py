class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called , Emplpyee deleted")
obj = Employee()
del obj