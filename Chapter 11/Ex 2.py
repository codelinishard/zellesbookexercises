#edited writeStudents to use f strings, and added gpa to display because I like that output's look more
# if gpa and credits can be sorted from lowest to highest,
#dictionary = {'gpa':Student.gpa,'name':Student.getName,'credits':Student.getHours}
#data.sort(key=dictionary[third],)
#data.sort(key=dictionary[second])
#data.sort(key=dictionary[first])

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
    return [x.strip().lower() for x in input("""Decide sort order, from highest to lowest importance.
The options are gpa, name, credits, separated by commas: """).split(",")]
    

def main():
    print("This program sorts student grade information by GPA,name, and credits")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    first,second,third = sortStudents() 
    reverseCheck = {'gpa':Student.gpa,'credits':Student.getHours}
    data.sort(key=reverseCheck.get(third,Student.getName), reverse = third in reverseCheck)
    data.sort(key=reverseCheck.get(second,Student.getName), reverse = second in reverseCheck)
    data.sort(key=reverseCheck.get(first,Student.getName), reverse = first in reverseCheck)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
