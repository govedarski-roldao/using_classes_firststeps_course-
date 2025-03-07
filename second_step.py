from random import randint
from main import DrawRectangle


# class Paint:
#     def __init__(self, buckets, color):
#         self.buckets = buckets
#         self.color = color
#
#     def total_price(self):
#         if self.color == "white":
#             return self.buckets * 1.99
#         else:
#             return self.buckets * 2.19


# class House:
#     def __init__(self, wall_area):
#         self.area = wall_area
#
#     def paint_needed(self):
#         return self.area * 2.5
#
#
# first_house = House(50)
# area = first_house.paint_needed()
# print(area)
# new_price = Paint(5, "yellow")
# price = new_price.total_price()
# print(price)
#


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


point1 = Point(6, 7)
point2 = Point(2, 2)


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def calculate_area(self):
        area = (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

    def guessed_area(self, guess):
        area = float(self.calculate_area())
        if guess > area:
            print(f"You choose to high, the area was {area}")
        elif guess < area:
            print(f"You choose to low, the area was {area}")
        else:
            print("Correct")


pointx = Point(6, 7)
rectangle_x = Rectangle(Point(5, 6), Point(7, 9))

rectangle_two = Rectangle(Point(randint(-200, 100), randint(-200, 100)), Point(randint(100, 190), randint(100, 190)))
print(
    f'Rectangle coordinates: {rectangle_two.lowleft.x}, {rectangle_two.lowleft.y} and {rectangle_two.upright.x}, {rectangle_two.upright.y}')
drawing = DrawRectangle(rectangle_two)
drawing.draw()
user_point = Point(float(input("Guess X:")), float(input("Guess Y:")))
print("Your point was inside of the rectange:", user_point.falls_in_rectangle((rectangle_two)))

guess_area = float(input("Please, try to guess the area of the rectangle:"))
rectangle_two.guessed_area(guess_area)
