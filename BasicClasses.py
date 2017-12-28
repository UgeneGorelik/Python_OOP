#Basic study of Class cration

#create Empty Class
class Employee_Empty:
    pass

#Class Employee
class Employee:

#class Variables
    employeeNumber=0
    raiseBy=10

#constructor that gets fname and salary variables
# and consturcts class variables (self = of this class)
    def __init__(self,fname,salary):
        self.fname=fname
        self.salary=salary
#increase class variable by 1 each time new instance created
        Employee.employeeNumber+=1

#class function
    def sayWord(self,word):
        print(self.fname+' '+word)

    def raiseSalaryOne(self):
        self.salary+=20

    def raiseSalaryTwo(self):
        self.salary+=Employee.raiseBy


#init instance of class
e1=Employee('avi',5)

e2=Employee('Eli Gelman',1000000)

#edit class variable
Employee.raiseBy+=10

e2.sayWord('says hi')

e2.raiseSalaryTwo()

#print insatnce and class as dict
print(e2.__dict__)

print(Employee.__dict__)