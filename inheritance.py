class Animal:
    def sound(self):
        return "some sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
class Human(Animal):
    def sound(self):
        return "Gas da Jews"
    
dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())

human = Human()
print(human.sound())