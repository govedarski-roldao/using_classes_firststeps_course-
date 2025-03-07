# import folium
#
# azores = folium.folium.Map(location=(38,-27),
#                            zoom_start=6)
#
# print (type(azores))

import turtle


class DrawRectangle:
    def __init__(self, rec):
        self.starting_position = rec.lowleft
        self.horizontal = rec.upright.x - rec.lowleft.x
        self.vertical = rec.upright.y - rec.lowleft.y
        self.my_turtle = turtle.Turtle()

    def draw(self):
        self.my_turtle.penup()
        self.my_turtle.goto(self.starting_position.x, self.starting_position.y)
        self.my_turtle.pendown()
        self.my_turtle.forward(self.horizontal)
        self.my_turtle.left(90)
        self.my_turtle.forward(self.vertical)
        self.my_turtle.left(90)
        self.my_turtle.forward(self.horizontal)
        self.my_turtle.left(90)
        self.my_turtle.forward(self.vertical)
        self.my_turtle.penup()

        turtle.done()

    def point_guessed(self, value):
        self.my_turtle.goto(value.x, value.y)
