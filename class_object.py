class Car:
    def __init__(self,model,colour):
        self.model = model
        self.colour = colour
        
    def display_info(self):
        print(f'Model : {self.model}, Colour : {self.colour}')
        
        
car1 = Car("Toyota","RED")
car1.display_info()