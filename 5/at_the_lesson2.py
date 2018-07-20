class Square:
    def __init__(self, side):
        print('Square has been created!')
        self.side = side

    def calc_perimeter(self):
        return self.side * 4

    def calc_area(self):
        return self.side * self.side


class Rectangle():
    def __init__(self, side_1, side_2):
        print('Rectangle has been created!')
        self.side_1 = side_1
        self.side_2 = side_2

    def calc_perimeter(self):
        return (self.side_1 + self.side_2) * 2

    def calc_area(self):
        return self.side_1 * self.side_2

class Triangle():
    def __init__(self, side_1, side_2, side_3):
        print('Triangle has been created!')
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def calc_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    #def calc_area(self, side_1, side_2, side_3):
    #    return side_1 * side_2

class Polygon:
    def __init__(self, side_1, side_2, side_3, side_4):
        print('Polygon has been created!')
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.side_4 = side_4

    def calc_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3 + self.side_4


def calculate_and_print(inpeut_data):
    if len(input_data) == 1:
        side = int(input_data)

        square_1 = Square(side)
        print('Perimeter of the square is {}'.format(square_1.calc_perimeter()))
        print('Area of the square is {}'.format(square_1.calc_area()))

    elif len(input_data) == 3:
        side_1 = int(input_data[0])
        side_2 = int(input_data[2])

        rectangle_1 = Rectangle(side_1, side_2)
        print('Perimeter of the rectangle is {}'.format(rectangle_1.calc_perimeter()))
        print('Area of the rectangle is {}'.format(rectangle_1.calc_area()))

    elif len(input_data) == 5:
        side_1 = int(input_data[0])
        side_2 = int(input_data[2])
        side_3 = int(input_data[4])

        triangle_1 = Triangle(side_1, side_2, side_3)
        print('Perimeter of the triangle is {}'.format(triangle_1.calc_perimeter()))

    elif len(input_data) == 7:
        side_1 = int(input_data[0])
        side_2 = int(input_data[2])
        side_3 = int(input_data[4])
        side_4 = int(input_data[6])

        polygon_1 = Polygon(side_1, side_2, side_3, side_4)
        print('Perimeter of the polygong is {}'.format(polygon_1.calc_perimeter()))

input_data = input('Enter data: ')

calculate_and_print(input_data)