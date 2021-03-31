class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perim = 2*self.width + 2*self.height
        return perim

    def get_diagonal(self):
        diag = (self.width ** 2 + self.height ** 2) ** .5
        return diag

    def get_picture(self):

        if self.height > 50 or self.width > 50 :
            pic = 'Too big for picture.'
        else:
            pic = self.height * (self.width * '*' + '\n')

        return pic

    def __str__(self):
        string_rep = 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
        return string_rep

    def get_amount_inside(self, shape):
        inside = self.get_area() // shape.get_area()
        return inside

class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

    def __str__(self):
        string_rep = 'Square(side=' + str(self.side) + ')'
        return string_rep


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(side=2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

sq.set_width(4)
print(sq)
