# I misread the question and didn't creat a single object and sorted with a different method. Think this works fine though.
def cardsort(filename):
    decklist = formatfile(filename) #file converted to list with (rank, suit) as element
    suitlists = suitsort(decklist) #split into four suits
    for suit in suitlists:
        valuesort(suit)
    finallist = recombination(suitlists)
    return finallist
def formatfile(filename):
    file = open(filename,"r")
    formattedlist = []
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        formattedlist.append(line)
    return formattedlist

def suitsort(decklist):
    dia = []
    club = []
    heart = []
    spade =[]
    for card in decklist:
        if card[0] == "diamonds":
            dia.append(card)
        if card[0] == "clubs":
            club.append(card)
        if card[0] == "hearts":
            heart.append(card)
        if card[0] == "spades":
            spade.append(card)
    return [dia,club,heart,spade]

def valuesort(suit):
    suit.sort(key = secondelement)
    
def secondelement(list):
    return list[1]

def recombination(suitlists):
    # a direct append can be done, because suitlists were already in order of size.
    combinedlist = []
    for suit in suitlists:
        for cards in suit:
            combinedlist.append(cards)
    return combinedlist

if __name__ == "__main__":
    print("This function sorts a list of cards in a file and returns the ordered list")
    filename = input("Provide the filename holding the unordered cards: ")
    finallist = cardsort(filename)
    print("The ordered list is")
    print(finallist)