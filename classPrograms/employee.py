# Consider a scenario where you have a base class called Employee and derived classes such as Manager, Engineer, and Salesperson.
# How would you handle implementing a common method, such as calculateSalary(), in each derived class using inheritance and method overriding

class Employee():
   def __init__(self ,salary):
       self.baseSalary = salary
   
class Manager(Employee):
    super.__init__()
    def __init__(self ,name,age,incentive):
       self.incenetive = incentive
       self.name = name
       self.age = age
    def calculateSalary(self):
        print(f' name : {self.name} /n age : {self.age}/n manager salary : {self.incenetive+self.baseSalary}')
    

#    calculateSalary('manager')
class Engineer(Employee):
    pass
class Salesperson(Employee):

    pass
obj = Employee(20000)
managerObj = Manager('akash',20,2000)
managerObj.calculateSalary()
