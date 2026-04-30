# ported my Chapter 9 Ex 8 adjusted for the new class 
import random

class Deck:
    def __init__(self):
        self.deck = [("Diamonds", 1), ("Diamonds", 2), ("Diamonds", 3), ("Diamonds", 4), ("Diamonds", 5), ("Diamonds", 6), ("Diamonds", 7), ("Diamonds", 8), ("Diamonds", 9), ("Diamonds", 10), ("Diamonds", "Jack"), ("Diamonds", "Queen"), ("Diamonds", "King"),
                     ("Clubs", 1), ("Clubs", 2), ("Clubs", 3), ("Clubs", 4), ("Clubs", 5), ("Clubs", 6), ("Clubs", 7), ("Clubs", 8), ("Clubs", 9), ("Clubs", 10), ("Clubs", "Jack"), ("Clubs", "Queen"), ("Clubs", "King"),
                     ("Hearts", 1), ("Hearts", 2), ("Hearts", 3), ("Hearts", 4), ("Hearts", 5), ("Hearts", 6), ("Hearts", 7), ("Hearts", 8), ("Hearts", 9), ("Hearts", 10), ("Hearts", "Jack"), ("Hearts", "Queen"), ("Hearts", "King"),
                     ("Spades", 1), ("Spades", 2), ("Spades", 3), ("Spades", 4), ("Spades", 5), ("Spades", 6), ("Spades", 7), ("Spades", 8), ("Spades", 9), ("Spades", 10), ("Spades", "Jack"), ("Spades", "Queen"), ("Spades", "King")]
    def shuffle(self):
        random.shuffle(self.deck)
    def dealCard(self,position):
        cardinfo = self.deck[position]
        self.deck.remove(self.deck[position])
        return cardinfo
    def cardsLeft(self):
        return len(self.deck)

def blackjack():
    printIntro()
    n = int(input("input the number of simulations to do: "))
    busts = simNgames(n)
    printSummary(n,busts)

def printIntro():
    print("This programme calculates the odds a player/dealer goes bust in blackjack")
    print("The simulated dealer will take cards until at least 17 is drawn")
    print("Aces are counted as 11 only if the results become 17 to 21, otherwise it's 1")

def simNgames(n):
    busts = 0
    for i in range(n):
        result = simOneGame()
        if result:
            busts += 1
    return busts

def simOneGame():
    # pool containing all the cards (thus their odds of being drawn)
    playingdeck = Deck()
    playingdeck.shuffle()
    hand = 0
    hasAce = 0 #0 is false
    while hand < 17: #once 17 is reached the dealer stops drawing
        newCard = playingdeck.dealCard(0)
        if newCard[1] == 1:
            hasAce += 1
            hand += 11
        else: 
            if newCard[1] in ["Jack", "Queen", "King"]:
                hand += 10
            else:
                hand += newCard[1]
        while hand > 21 and hasAce >= 1:
            hand = hand - 10
            hasAce = hasAce - 1
    if hand > 21:
        return True
    else: return False 

def printSummary(n,busts):
    print(f"In {n} games, the dealer busted {busts} times.")
    print(f"The probability the dealer busts is {busts/n:.1%}" )

blackjack()