class Shape:
    def __init__(self,colour,is_filled):
        self.colour = colour 
        self.is_filled = is_filled

    def describe(self):
        print(f"Its is {self.colour} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self,colour,is_filled,radius):
        super().__init__(colour,is_filled)
        self.radius = radius
        
    def describe(self):
        super().describe()
        print(f"it is a circle and the area is {3.1416 * self.radius * self.radius} CM^2")
        
    
class Square(Shape):
    def __init__(self,colour,is_filled,width):
        super().__init__(colour,is_filled)
        self.width = width
        
    def describe(self):
        super().describe()
        print(f"it is a square and the area is {self.width * self.width} CM^2")
        
    
class Triangle(Shape):
    def __init__(self,colour,is_filled,width,height):
        super().__init__(colour,is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        super().describe()
        print(f"it is a triangle and the area is {0.5 * self.width * self.height} CM^2")
        
        
circle = Circle(colour="red",is_filled=True,radius=5)
square = Square(colour="red",is_filled=False,width=8)
triangle = Triangle(colour="red",is_filled=True,width=5,height=4)


print(circle.colour)
print(square.width)
print(f"my height is 5 feet {triangle.height} INCH")

circle.describe()
square.describe()
triangle.describe()