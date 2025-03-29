from random import randint
import turtle


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
        print(area)

    def guessed_area(self, guess):
        area = float(self.calculate_area())
        if guess > area:
            print(f"You choose to high, the area was {area}")
        elif guess < area:
            print(f"You choose to low, the area was {area}")
        else:
            print("Correct")


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        self.starting_position = self.lowleft
        self.horizontal = self.upright.x - self.lowleft.x
        self.vertical = self.upright.y - self.lowleft.y
        canvas.penup()
        canvas.goto(self.starting_position.x, self.starting_position.y)
        canvas.pendown()
        canvas.forward(self.horizontal)
        canvas.left(90)
        canvas.forward(self.vertical)
        canvas.left(90)
        canvas.forward(self.horizontal)
        canvas.left(90)
        canvas.forward(self.vertical)
        canvas.penup()
        turtle.done()


class GuiPoint(Point):
    def mark_point(self, canvas):
        canvas.goto(self.)

# Get the choice from user
user_point = Point(float(input("Guess X:")), float(input("Guess Y:")))
guess_area = float(input("Please, try to guess the area of the rectangle:"))
# print the same result
gui_rectangle = GuiRectangle(Point(randint(-200, 200), randint(-200, 200)), Point(randint(100, 190), randint(100, 190)))

# Construct the gui
myturle = turtle.Turtle()
gui_rectangle.draw(myturle)
gui_rectangle.calculate_area
