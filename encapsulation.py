class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    
emp1 = Employee("john",500)
print(emp1.get_salary())