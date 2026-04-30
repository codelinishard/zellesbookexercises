# thought about making the program more modular, but honestly, it seems like a lot more work for no gain

from gpa import Student, makeStudent
from graphics import *
from button import *
def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print(f"{s.getName():<20}{(s.gpa()):<10}{s.getHours():<10}{s.getQPoints():<10}", file=outfile)
    outfile.close()
                    

def main():
    win = GraphWin("student sorting", 600, 600)
    win.setBackground("white")
    win.setCoords(0,0,20,20)
    #labels and entries
    introText = Text(Point(10,18.5),"""This program sorts student grade information by GPA, name, and credits
            You can decide whether the list is by ascending or descending order for each option.
            Choose from sort first to last, so if GPA is lowest importance, choose it first.
            After filling out the details, click 'Proceed' button to produce output.""")
    insertLabel = Text(Point(2,5),"Name of inputfile")
    insertName = Entry(Point(6,5),10)
    outputLabel = Text(Point(2,2),"Name of outputfile")
    outputName = Entry(Point(6,2),10)
    introText.draw(win)
    outputLabel.draw(win)
    insertLabel.draw(win)
    insertName.draw(win)
    outputName.draw(win)

    #buttons for sorting
    gpaButton = Button(win, Point(3,12), 2, 1.5, "GPA")
    gpaAscend = Button(win, Point(3,10), 2, 1.5, "Ascend")
    gpaDescend = Button(win, Point(3,8), 2, 1.5, "Descend")
    nameButton = Button(win, Point(10,12), 2, 1.5, "Name")
    nameAscend = Button(win, Point(10,10), 2, 1.5,  "Ascend")
    nameDescend = Button(win, Point(10,8), 2, 1.5, "Descend")
    creditButton = Button(win, Point(17,12), 2, 1.5, "Credits")
    creditAscend = Button(win, Point(17,10), 2, 1.5, "Ascend")
    creditDescend = Button(win, Point(17,8), 2, 1.5, "Descend")
    resetButton = Button(win,Point(10,2),2,1.5, "reset")
    quitButton = Button(win,Point(18,2), 2, 1.5, "Proceed")
    sortTypeList = [gpaButton,nameButton,creditButton]
    sortMethodList = [gpaAscend,gpaDescend,nameAscend,nameDescend,creditAscend,creditDescend]

    typeOrdering = [] #collects the sorting order decided
    methodOrdering = [] #collects the sorting method decided

    resetButton.activate()
    quitButton.activate()
    allbuttons = sortTypeList + sortMethodList
    for i in allbuttons:
        i.activate()
    

    while True:
        p= win.getMouse()
        for i in sortMethodList:
            if i.clicked(p):
                methodOrdering.append(i)
                i.deactivate()
        
        for i in sortTypeList:
            if i.clicked(p):
                typeOrdering.append(i)
                i.deactivate()
        
        if resetButton.clicked(p):
            methodOrdering.clear()
            typeOrdering.clear()
            for i in allbuttons:
                i.activate()
        
        if quitButton.clicked(p):
            break


    ascendCheck = [gpaAscend,nameAscend,creditAscend]
    insert = insertName.getText()
    output = outputName.getText()
    data = readStudents(insert)
    dictionary = {'GPA':Student.gpa,'Name':Student.getName,'Credits':Student.getHours}
    for i in range(3):
        data.sort(key=dictionary[typeOrdering[i].getLabel()],reverse = (methodOrdering[i] in ascendCheck))
    writeStudents(data, output)
    End = Text(Point(10,16),f"The data has been written to {output} click anywhere to close")
    End.draw(win)
    win.getMouse()
    win.close()
    return
if __name__ == '__main__':
    main()
