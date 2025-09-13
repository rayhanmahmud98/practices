class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.1316 * self.radius ** 2
    
    
circle1 = Circle(5)
print("area : ", circle1.area())