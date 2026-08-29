# A lot more work than expected went into preparing the files for spellchecking. 
# Due to dictionary limitations, words with punctuation inside cannot be identified
def full_dict():
	full_list = []
	with open("dolph's dict.txt") as f:
		for line in f:
			full_list.append(line.strip())
	return full_list

def check(word, dict_to_use):
	if len(dict_to_use) == 1:
		if word == dict_to_use[0]:
			return True
		else: return False
	else:
		no = len(dict_to_use)//2
		if word != dict_to_use[no]:
			if word < dict_to_use[no]:
			# go lower
				return check(word,dict_to_use[:no])
			elif word > dict_to_use[no]:
			#go higher``
				return check(word,dict_to_use[no:])
		else: #found it
			return True

def getfile():
	file = []
	#file_name = input("What file do you want to spellcheck?")
	file_name = "test_file.txt"
	with open(file_name) as f:
		for line in f:
			if line == "\n":
				continue
			line = line.split()
			for word in line:
				word = word.strip("!#$%&'()*+,-./:;<=>?@[^_`{|}~\\]\"\n")
				if word != "":
					file.append(word)
	return file

def str_converter(errors):
	string = ""
	for i in range(len(errors)):
		if i == 0:
			string += errors[i]
		else:
			string += f", {errors[i]}"
	return string

if __name__ == "__main__":
	errors = []
	file = getfile()
	dictionary = full_dict()
	for text in file:
		result = check(text.lower(), dictionary)
		if result == False:
			if text not in errors:
				errors.append(text)
	if errors != "":
		print("There were errors in the text.")
		errors = str_converter(errors)
		print(f"The unrecognised words are {errors}")
	else:
		print("There was no error with the text")