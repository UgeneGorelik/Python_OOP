#further investigation of Classes


class Employee:

    employeeNumber=0
    raiseBy=10

    def __init__(self,fname,salary):
        self.fname=fname
        self.salary=salary
        Employee.employeeNumber+=1

#A class method is a method that is bound to a class rather than its object.
#  It doesn't require creation of a class instance, much like staticmethod.
    @classmethod
    def set_raise(cls,num):
        cls.raiseBy=num

#we create constuctor by using static method (Usefull in Factory design pattern btw)
    @classmethod
    def CreateConstructorAsMethod(cls,fname,salary):
        return  cls(fname+" created from classmethod",salary)


#Static method knows nothing about the class and just deals with the parameters
    @staticmethod
    def smethod():
        print("I dont know a thing of the Class i am in")


e1=Employee.CreateConstructorAsMethod('Eli',10000)

print(e1.__dict__)

Employee.smethod()