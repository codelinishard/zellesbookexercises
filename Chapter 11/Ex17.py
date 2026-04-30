#makeFace from Chapter 4 Ex 3
from graphics import *
class GraphicsGroup:
    def __init__(self,anchor):
        self.anchor = anchor
        self.grouplist = []
    def getAnchor(self):
        return self.anchor
    def addObject(self,gObject):
        self.grouplist.append(gObject)
    def move(self,dx,dy):
        self.anchor.move(dx,dy)
        for gObject in self.grouplist:
            gObject.move(dx,dy)
    def draw(self,win):
        for gObject in self.grouplist:
            gObject.draw(win)
    def undraw(self):
        for gObject in self.grouplist:
            gObject.undraw()

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""
    
    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit')"""
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
    
    def clicked(self, p):
        """Returns true if p is inside"""
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

def makeFace(win, classgroup,center):
        #defining the circles to draw first
        x, y = center.getX(), center.getY()
        face = Circle(center,5)
        face.setFill("white")
        face.setOutline("black")
        Leyes = Circle(Point(x - 2.0, y + 2.0),1)
        Leyes.setOutline("black")
        Lpup = Circle(Point(x - 2.0, y + 2.0),0.5)
        Lpup.setFill("black")
        Rpup = Lpup.clone()
        reyes = Leyes.clone()
        reyes.move(4,0)
        Rpup.move(4,0)
        Nose = Polygon(Point (x , y),Point(x , y + 2),Point(x+1 , y + 1))
        Mouth = Oval(Point(x - 2, y - 1),Point(x + 2, y - 1))
        
        itemList = [face, Leyes, Lpup, Rpup, reyes, Nose, Mouth]
        for item in itemList:
            classgroup.addObject(item)
            item.draw(win)
        
def main():
    win = GraphWin("Face", 800, 800)
    win.setCoords(0,0,28,28)
    Title = Text(Point(7.0,13.0), "Click to move the face").draw(win)
    classgroup = GraphicsGroup(Point(7.0,7.0))
    makeFace(win, classgroup, Point(7.0,7.0))
    quit = Button(win, Point(7.0, 1.0), 5.0, 2.0, "Quit")
    while True:
        p = win.getMouse()
        if quit.clicked(p):
            break 
        x, y = p.getX(), p.getY()
        classgroup.move(x - classgroup.getAnchor().getX(), y - classgroup.getAnchor().getY())
    Title.undraw()
    Title.setText("Stopping programme. Click again to close the window.")
    Title.draw(win)
    win.getMouse()
    win.close()

main()

