class card:

    ranks = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13}
    suits = {"diamond":1, "clubs":2, "hearts":3, "spades":4}
    def __init__(self,suit,rank):
        self.rank = rank
        self.cardvalue = self.ranks[rank]
        self.suit = suit
        self.suitvalue = self.suits[suit]
    
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def rankvalue(self):
        return self.cardvalue
    def suitValue(self):
        return self.suitvalue
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __repr__(self):
        return self.__str__()


def cardsort(filename):
    cardlist = listConverter(filename) # returns a list
    cardlist = classConverter(cardlist) #converts elements into card class
    cardlist.sort(key = card.rankvalue)
    cardlist.sort(key = card.suitValue)
    return cardlist

def listConverter(filename):
    file = open(filename,"r")
    formattedlist = []
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        formattedlist.append(line)
    return formattedlist

def classConverter(cardlist):
    updatedList = []
    for n in cardlist:
        obj = card(n[0],n[1])
        updatedList.append(obj)
    return updatedList

def handIdentifier(cardlist):
    ranklist = []
    suitlist = []
    for cards in cardlist:
        ranklist.append(cards.rankvalue())
        suitlist.append(cards.suitValue())

    if all(x == suitlist[0] for x in suitlist): 
        if ranklist == [1,10,11,12,13]: #cardlist was already sorted beforehand
            return "Royal Flush"
        elif ranklist == [ranklist[0],ranklist[0]+1,ranklist[0]+2, ranklist[0]+3,ranklist[0]+4]: #straight flush
            return "Straight Flush"
        else: # just flush
            return "flush"
    else:
        thinned, uniques = countDuplicates(suitlist) #as there are 5 cards, len() being 3 means quads or triple. 2 means triple or 2 pair, and 1 means pair
        
        if ranklist == [ranklist[0],ranklist[0]+1,ranklist[0]+2, ranklist[0]+3,ranklist[0]+4]:
            return "Straight"
        
        if len(thinned) == 3 and uniques == 2 and len(countDuplicates(thinned)[1]) == 2:
            return "Full house"
        elif len(thinned) == 3 and uniques == 2 and len(countDuplicates(thinned)[1]) == 1:
            return "Four of a Kind"
        elif len(thinned) == 2 and uniques == 3 and len(countDuplicates(thinned)[1]) == 1:
            return "Three of a kind"
        elif len(thinned) == 2 and uniques == 3 and len(countDuplicates(thinned)[1]) == 2:
            return "Two pair"
        else: 
            return f"{ranklist[-1]} High"
    
def countDuplicates(somelist): #Ex 7 renamed and with a return 
    i = 0
    uniques = []
    dupe_list = []
    for i in range(len(somelist)):
        if somelist[i] not in uniques:
            uniques.append(somelist[i])
        elif somelist[i] in uniques:
            dupe_list.append(somelist[i])
    return dupe_list, uniques

if __name__ == "__main__":
    print("This function takes a list of 5 cards in a file and returns the ordered list")
    print("It will also identify what is the poker hand")
    filename = input("Provide the filename holding the unordered cards: ")
    finallist = cardsort(filename)
    pokerhand = handIdentifier(finallist)
    print(f"The ordered list is {finallist}")
    print(f"The poker hand is {pokerhand}")