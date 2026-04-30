# reused class with minor dictionary tweaks
class card:

    ranks = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13}
    suits = {"diamonds":1, "clubs":2, "hearts":3, "spades":4}
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


if __name__ == "__main__":
    print("This function sorts a list of cards in a file and returns the ordered list")
    filename = input("Provide the filename holding the unordered cards: ")
    finallist = cardsort(filename)
    print("The ordered list is")
    print(finallist)

    