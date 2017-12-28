#Example of using Dunder method (sort of operator overloading resemblig from c++ but not
#tottaly similair
#property setter

class Animal:

    AnimalNumber=0

    def __init__(self,aname,atype,flee):
        self.aname=aname
        self.atype=atype
        self.hasflees=flee

        Animal.AnimalNumber+=1
    #Dunder methods (magic methods)

    #sort of C++ add operator overload
    def __add__(self, other):
              return  ("we are a pack now "+self.aname + " "+other.aname)

    #reprt
    def __repr__(self):
        return ("i am Dunder "+self.aname)

    #sort of to string operator

    def __str__(self):
        return ("i am Dunder "+self.aname)


   #decalre hasflees to be a property
   #make note of underscore it HAVE TO BE there if you want to be initiated from construcor
   #sort of private variable but it is not realy private so dont count on it

    @property
    def hasflees(self):
        return self._hasflees

    #the setter itself
    @hasflees.setter
    def hasflees(self,value,):
         self._hasflees=value


a1=Animal('Fluff','dogski','Need to go to VEt')

a2=Animal('Scratch','hatulski','no flees')


print(a1)

print(str(a1))

print(a1+a2)

print(a1.hasflees)
