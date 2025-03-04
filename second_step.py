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

    def falls_in_rectangle(self,rectangle):
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


pointx = Point(6, 7)
rectanglex = Rectangle(Point(5, 6), Point(7, 9))
pointx.falls_in_rectangle(rectanglex)
