def censor(filename,censorFileName):
	infile = open(filename,'r')
	censorFile = open(censorFileName, "r")
	censorList = readNformat(censorFile)
	bigList = readNformat(infile) #converts each line into a minilist
	infile.close()
	censoringProgramme(bigList,censorList) # for n in list, for term in minilist, if len(3), censor
	outname = input("What will the name of the file with censors be? ")
	finalFile = fileRecreation(bigList, outname) #create new file and print out
	return finalFile

def readNformat(infile):
	formatted = []
	for line in infile:
		minilist = line.split()
		minilist = [string.strip(",.!?:;") for string in minilist]
		formatted.append(minilist)
	return formatted
	
def censoringProgramme(bigList,censorList):
	for smallList in bigList:
		pos = 0 #position of element in smallList
		for term in smallList:
			if term in censorList:
				smallList[pos] = "*" * len(term)
			pos += 1

def fileRecreation(editedList,outname):
		outfile = open(outname,"w")
		for lists in editedList:
			print(*lists, sep = " ", file = outfile)
		outfile.close()
		return outfile

if __name__ == "__main__":
	print("This programme censors words from a file using another file containing words to censor. ")
	filename = input("What is the name of the file to censor?: ")
	censorfilename = input("What is the name of the file to use for censoring?: ")
	censor(filename,censorfilename)
	print("Done.")