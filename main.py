# import folium
#
# azores = folium.folium.Map(location=(38,-27),
#                            zoom_start=6)
#
# print (type(azores))

import turtle


class DrawRectangle:
    def __init__(self, rec):
        self.horizontal = rec.upright.x - rec.lowleft.x
        self.vertical = rec.upright.y - rec.lowleft.y

    def draw(self):
        my_turtle = turtle.Turtle()
        my_turtle.forward(self.horizontal)
        my_turtle.left(90)
        my_turtle.forward(self.vertical)
        my_turtle.left(90)
        my_turtle.forward(self.horizontal)
        my_turtle.left(90)
        my_turtle.forward(self.vertical)
        my_turtle.penup()

        turtle.done()




