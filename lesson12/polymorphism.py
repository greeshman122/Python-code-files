class cat:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def info(self):
        print("The cat (Felis catus), also referred to as the domestic cat or house cat, is a small domesticated carnivorous mammal. ")
        print("Cat name : " , self.name)
        print("Cat age : " , self.age)
    def make_sound(self):
        print("I sound like meow meow")
class dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def info(self):
        print("The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the gray wolf. Also called the domestic dog, it was selectively bred from an extinct population of wolves during the Late Pleistocene by hunter-gatherers.")
        print("Dog name : " , self.name)
        print("Dog age : " , self.age)
    def make_sound(self):
        print("I sound like . bow bow ")
c = cat("Narshima" , 2)
c.info()
c.make_sound()
d = dog("Rocky" , 2)
d.info()
d.make_sound()