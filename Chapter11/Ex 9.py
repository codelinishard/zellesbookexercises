# a LIST of tuples. I was wondering how I could sort anything if I had to make a tuple.

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
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), 
              file=outfile)
    outfile.close()
                      
def sortPrep(students):
    tupl = []
    for n in students:
        tupl.append((n.gpa(),n))
    return tupl

def rebuiltlist(tupl):
    students = []
    for n in tupl:
        students.append(n[1])
    return students

def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data = sortPrep(data)
    data.sort()
    data = rebuiltlist(data)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
