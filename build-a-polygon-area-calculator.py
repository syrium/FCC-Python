import math

class RangeError(Exception):
    """To raise erorr when width or height is larger than 50"""
    pass

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    #@property
    #def set_width(self):
    #    return self._width

    #@set_width.setter
    def set_width(self, width:float):
       self._width = width
       return self._width

    #@property
    #def set_height(self) -> float:
    #    return self._height
    
    #@set_height.setter
    def set_height(self, height) -> None:
        self._height = height
        return self._height

    def get_area(self) -> float:
        return self._width*self._height
    
    def get_perimeter(self) -> float:
        return 2*(self._width + self._height)
    
    def get_diagonal(self) -> float:
        return math.sqrt(self._width**2 + self._height**2)

    def get_picture(self) -> str:
        shape = ''
        if (self._width >= 50) or (self._height >= 50):
            return 'Too big for picture.'
        for h in range(self._height):
            for w in range(self._width):
                shape += '*'
            shape += '\n'
        return shape
    
    def get_amount_inside(self, shape) -> int :
        return 0 if self.get_area()<shape.get_area() else self.get_area() // shape.get_area()

    def __str__(self) -> str:
        return f'Rectangle(width={self._width}, height={self._height})'

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self._side_length = side_length
    
    def set_width(self, side_length:float) -> None:
        self._side_length = side_length
    
    def set_height(self, side_length:float) ->None:
        self._side_length = side_length
    
    def set_side(self, side_length:float) -> None:
        self._side_length = side_length
        self._height = self._side_length
        self._width = self._side_length
    
    def __str__(self) -> str:
        return f'Square(side={self._side_length})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
sq.set_width(6)
print(sq)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))