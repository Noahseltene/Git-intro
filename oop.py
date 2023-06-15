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
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def describe(self):
        print("This is a {}".format(self.name))
    def know(self):
        print("The {} is {} years old".format(self.name, self.age))

a=School("director",56)
b=School("student",14)
c=School("teacher",34)
a.describe()
b.describe()
c.describe()
b.know()
a.know()
c.know()
        

  
    
        


