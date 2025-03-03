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

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


point1 = Point(1, 1)
point2 = Point(2, 2)


print(Point(3, 4).falls_in_rectangle((5, 6), (7, 9)))
