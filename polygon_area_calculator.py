"""This module contains classes to calculate areas and properties
of polygons like rectangles and squares."""
class Rectangle:
    """Class representing a rectangle shape."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """Set the width of the rectangle."""
        self.width = width

    def set_height(self, height):
        """Set the height of the rectangle."""
        self.height = height

    def get_area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Calculate the diagonal length of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Generate a string representation of the rectangle using '*' characters."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        """Calculate how many times the given shape fits inside this rectangle."""
        # how many times `shape` fits in this rectangle (no rotation)
        if shape.width == 0 or shape.height == 0:
            return 0
        fit_across = self.width // shape.width
        fit_down = self.height // shape.height
        return fit_across * fit_down

class Square(Rectangle):
    """Class representing a square shape, inheriting from Rectangle."""
    def __init__(self, side):
        super().__init__(side, side)  # initialize width and height from Rectangle
        self.side = side

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        """Set the side length of the square."""
        self.width = side
        self.height = side

    # Override width setters so Square stays valid
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

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

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
