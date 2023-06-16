class Animal():
    # pass
    # print("this is a class")
    breathe = "yes"
    # constructor it initialises a class
    def __init__(self,name,species):
        self.name=name #class properties
        self.species=species #class properties


    # class method
    def belongs(self):
        print("The mammal belongs to  {}".format(self.species))     

    def description(self):
        print("The name of the animal is {}".format(self.name))   


# a=Animal("cow","mammal")
# b=Animal("hen","bird")
# c=Animal("goat","mammal")   

# c.description()
# a.description()
# b.description()
class School():
    uname="University"


    def __init__(self,name,age):
        self.name=name
        self.age=age
    def describe(self, height):
        print("This is a {} and his height is {}".format(self.name,height))
    def know(self):
        print("The {} is {} years old".format(self.name, self.age))

# a=School("director",56)
# b=School("student",14)
# c=School("teacher",34)
# print(a.name)
# print(a.uname)

# a.describe("tall")
# b.describe()
# c.describe()
# b.know()
# a.know()
# c.know()

class Car():
    def __init__(self,model,color):
        self.color=color
        self.model=model
    def display(self):
        print("Type of the car is {} and its {} ".format(self.model, self.color))
    def colour(self):
        print("The car is {}".format(self.color))
f=Car("Toyota","Black")
d=Car("Nissan","Red")
r=Car("Ford","Silver")

f.display()
d.display()
r.display()
# f.colour()
# d.colour()
# r.colour()
        

  
    
        


