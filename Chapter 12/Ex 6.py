# I really have no idea what the question wants me to make. Should I be making 3 CPUs?
# I can't programme a simulation of a human reading each other's tells.

#I gave up. I don't grasp the bidding strategies to do for bridge. I'll write an update if I ever find myself playing bridge in the future I suppose
from random import shuffle
class card: #modified from chapter 10 Ex11

    ranks = {14:"Ace",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen",13:"King"}
    suits = {"d":"diamond","c":"clubs","h":"hearts","s":"spades"}
    def __init__(self,rank,suit):
        if rank <= 10:
            self.cardvalue = 0
        elif rank >= 11:
            self.cardvalue = rank - 10
        
        self.rank = self.ranks[rank]
        self.suit = self.suits[suit]
    
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def value(self):
        return self.cardvalue
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class model:
    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.hand3 = []
        self.hand4 = []
    
    def generate_deck(self):
        suits = ["d","c","h","s"]
        self.deck = []
        for rank in range(2,15):
            for i in range(4):
                c = card(rank,suits[i])
                self.deck.append(c) 

    def shuffle(self,thing): 
        shuffle(thing)
        return thing # if needed
    
    def deal_hands(self):
        hands = [self.hand1,self.hand2,self.hand3,self.hand4]
        for hand in hands:
            for i in range(13): #13 cards per hand in a deck of 52
                c = self.deck.pop()
                hand.append(c)

    def setup(self):
        self.generate_deck()
        self.shuffle(self.deck)
        self.deal_hands()
        
    def determine_bid(self,hand):
        