#this was potentially the longest question in the book

from graphics import *
from math import pi, sin, cos, radians
class Turtle:

    def __init__(self):
        self.win = GraphWin("Koch", 800, 800)
        self.win.setBackground("darkgreen")
        self.win.setCoords(0,0,800,800)
        self.location = Point(400, 573.2)
        self.direction = radians(-120)

    def move_to(self, x,y):
        """updates location"""
        self.location = Point(x,y)

    def draw(self,length):
        """draws a line using current direction and location"""
        dx = self.location.getX() + length * cos(self.direction)
        dy = self.location.getY() + length * sin(self.direction)
        thing = Line(self.location, Point(dx, dy))
        thing.draw(self.win)
        return dx,dy

    def turn(self, angle):
        """angle adjustment is clockwise, and value is in degrees"""
        self.direction += radians(angle)

    def koch(self, length, degree):
        if degree == 0:
            dx,dy = self.draw(length)
            self.move_to(dx,dy)
        else:
            length1 = length/3
            degree1 = degree-1
            self.koch(length1, degree1)
            self.turn(-60)
            self.koch(length1, degree1)
            self.turn(120)
            self.koch(length1, degree1)
            self.turn(-60)
            self.koch(length1, degree1)

if __name__ == "__main__":
    snowflake = Turtle()
    for i in range(3):
        snowflake.koch(300,5)
        snowflake.turn(120)



