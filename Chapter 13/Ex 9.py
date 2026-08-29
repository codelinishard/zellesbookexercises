#this was potentially the longest question in the book

from graphics import *
from math import pi, sin, cos, radians
class Turtle:

    def __init__(self):
        self.win = GraphWin("C-curve", 800, 800)
        self.win.setBackground("darkgreen")
        self.win.setCoords(0,0,800,800)
        self.location = Point(350, 450)
        self.direction = radians(-90)

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
        """angle adjustment is clockwise, and angle taken is in degrees"""
        self.direction += radians(angle)

    def curve(self, length, degree):
        if degree == 0:
            dx,dy = self.draw(length)
            self.move_to(dx,dy)
        else:
            length1 = length/(2**0.5)
            degree1 = degree-1
            self.turn(-45)
            self.curve(length1, degree1)
            self.turn(90)
            self.curve(length1, degree1)
            self.turn(-45)

if __name__ == "__main__":
    snowflake = Turtle()
    for i in range(4):
        snowflake.curve(120,10)
        snowflake.turn(90)



