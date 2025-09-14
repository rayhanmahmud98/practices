class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary cant be negative")
    
    
    
emp1 = Employee("john",500)
print(emp1.get_salary())