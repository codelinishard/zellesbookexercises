def censor(filename):
	infile = open(filename,'r')
	bigList = readNformat(infile) #converts each line into a minilist
	infile.close()
	censoringProgramme(bigList) # for n in list, for term in minilist, if len(3), censor
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

def censoringProgramme(bigList):
	for smallList in bigList:
		pos = 0 #position of element in smallList
		for term in smallList:
			if len(term) == 4:
				smallList[pos] = "****"
			pos += 1

def fileRecreation(editedList,outname):
		outfile = open(outname,"w")
		for lists in editedList:
			print(*lists, sep = " ", file = outfile)
		outfile.close()
		return outfile

if __name__ == "__main__":
	print("This programme censors 4 word-length words from a file. ")
	filename = input("What is the name of the file to censor?: ")
	censor(filename)
	print("Done.")