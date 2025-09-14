class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduction(self):
        return f"HI , my name is {self.name} and I am {self.age} years old"

person1 = Person("Adolf",40)
person2 = Person("Hitler",25)

print(person1.introduction())
print(person2.introduction())    