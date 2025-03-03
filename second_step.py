# class Paint:
#     def __init__(self, buckets, color):
#         self.buckets = buckets
#         self.color = color
#
#
# class House:
#     def __init__(self, wall_area):
#         self.area = wall_area

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance(self, x, y):
        return abs(x - y)


point1 = Point(10, 20)
print(type(point1))
print(Point(3, 4).falls_in_rectangle((5, 6), (7, 9)))
