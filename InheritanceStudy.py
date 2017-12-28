#Example of Inheritance


class Animal:

    AnimalNumber=0

    def __init__(self,aname,atype):
        self.aname=aname
        self.atype=atype
        Animal.AnimalNumber+=1


    def sayHi(self):
       print('i am Animal')


#class Dog inherits from Animal
class Dog(Animal):
     def __init__(self,aname,atype,food):

#send aname and atype to the animal class which dog inherits from
         super().__init__(aname,atype)
         self.food=food

# overriding Animal Class function
     def sayHi(self):
         print('i am Dog')





d=Dog('Lasy','Dogski','shoes')

d.sayHi()

#check if dog is instance of animal
print(isinstance(Dog,Animal))
#check if dog is subclass of animal
print(issubclass(Dog,Animal))