# I really should have read the next question first

from gpa import Student, makeStudent

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
                      
def sortStudents():
    return [(x.strip().lower()) for x in input("""Decide sort order, from highest to lowest importance.
The options are gpa, name, credits, separated by commas: """).split(",")]

def sortOrder(): # x.strip() == "True" because the input is a string and to remove spacing
    return [(x.strip() == "True") for x in input("""Decide whether the 3 options are in
ascending(True) or descending(False). Separate the respective options with comma: """).split(",")]
    

def main():
    print("This program sorts student grade information by GPA,name, and credits")
    print("You can decide whether the list is by ascending or descending order for each option")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    studentOrder = sortStudents() 
    methodOrder = sortOrder()
    dictionary = {'gpa':Student.gpa,'name':Student.getName,'credits':Student.getHours}
    for i in range(0,3,-1):
        data.sort(key=dictionary[studentOrder[i]],reverse = methodOrder[i])
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
