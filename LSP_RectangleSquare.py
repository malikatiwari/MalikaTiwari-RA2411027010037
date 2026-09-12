class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


# Warm-up result: a Square stored as a Rectangle still behaves as a Square.
# Calling set_width(10) then set_height(20) makes both sides 20, so the area is 400.
# Expected for a normal Rectangle would be 10 * 20 = 200.

def rectangle_area(rectangle):
    rectangle.set_width(10)
    rectangle.set_height(20)
    return rectangle.get_area()


square_as_rectangle = Square()
print("Square stored as Rectangle area:", rectangle_area(square_as_rectangle))
