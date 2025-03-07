class parrot:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def sing(self , song):
        return "{} sings {}".format(self.anem , song)
    def dance(self):
        return "{} is now dancing".format(self.name)
blu = parrot("Blu" , 10)
print(blu.sing("'Happy'"))
print(blu.dance())