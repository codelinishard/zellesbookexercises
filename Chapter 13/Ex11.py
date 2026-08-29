# words to try: eat, stop, nlties, caters

def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

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
			#go higher
				return check(word,dict_to_use[no:])
		else: #found it
			return True

def str_converter(solutions):
	string = ""
	for i in range(len(solutions)):
		if i == 0:
			string += solutions[i]
		else:
			string += f", {solutions[i]}"
	return string

def handle_input():
	while True:
		word = input("What word do you want to check?: ")
		for x in word:
				if x in ["!#$%&'()*+,-./:;<=>?@[^_`{|}~\\]\"\n"]:
					print("No punctuation!")
					continue
				if x == "":
					print("Give me something to work with!!")
					continue
		return word.lower()
		
		

	
if __name__ == "__main__":
	valid_words = []
	print("This program returns all valid words with the letters you input.")
	word = handle_input()
	dictionary = full_dict()
	anagram_list = anagrams(word)
	for word in anagram_list:
		result = check(word, dictionary)
		if result == True:
			if word not in valid_words:
				valid_words.append(word)
	if valid_words != "":
		print("There were valid words in the input.")
		valid_words = str_converter(valid_words)
		print(f"The valid words are {valid_words}")
	else:
		print("There was valid words that I could make with your input :()")

