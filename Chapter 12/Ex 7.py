
#WAAAARRR
#class from chapter 11 ex 15
import random
from graphics import GraphWin, Point, Text, Image, Rectangle

class Deck:
    def __init__(self):
        self.deck = [("Diamonds", 1), ("Diamonds", 2), ("Diamonds", 3), ("Diamonds", 4), ("Diamonds", 5), ("Diamonds", 6), ("Diamonds", 7), ("Diamonds", 8), ("Diamonds", 9), ("Diamonds", 10), ("Diamonds", 11), ("Diamonds", 12), ("Diamonds", 13),
                     ("Clubs", 1), ("Clubs", 2), ("Clubs", 3), ("Clubs", 4), ("Clubs", 5), ("Clubs", 6), ("Clubs", 7), ("Clubs", 8), ("Clubs", 9), ("Clubs", 10), ("Clubs", 11), ("Clubs", 12), ("Clubs", 13),
                     ("Hearts", 1), ("Hearts", 2), ("Hearts", 3), ("Hearts", 4), ("Hearts", 5), ("Hearts", 6), ("Hearts", 7), ("Hearts", 8), ("Hearts", 9), ("Hearts", 10), ("Hearts", 11), ("Hearts", 12), ("Hearts", 13),
                     ("Spades", 1), ("Spades", 2), ("Spades", 3), ("Spades", 4), ("Spades", 5), ("Spades", 6), ("Spades", 7), ("Spades", 8), ("Spades", 9), ("Spades", 10), ("Spades", 11), ("Spades", 12), ("Spades", 13)]
    def shuffle(self):
        random.shuffle(self.deck)
    def dealCard(self,position = 0):
        cardinfo = self.deck[position]
        self.deck.remove(self.deck[position])
        return cardinfo
    def cardsLeft(self):
        return len(self.deck)
    def empty(self): #new method
        self.deck.clear()
    def append(self,card):
        self.deck.append(card)

class model():
    def __init__(self,interface):
        self.interface = interface
        self.deck1 = Deck()
        self.deck2 = Deck()
        self.deck2.empty()
        #deck2 takes half
        self.deck1.shuffle()
        for i in range(26):
            self.deck2.append(self.deck1.dealCard())
        self.update_counts()

    def update_counts(self):
        self.interface.update_deck_counts(self.deck1.cardsLeft(), self.deck2.cardsLeft())

    def run(self):
        while self.deck1.cardsLeft() != 0 and self.deck2.cardsLeft() != 0:
            deck1_card = self.deck1.dealCard()
            deck2_card = self.deck2.dealCard()
            self.interface.drawing_cards(deck1_card, deck2_card)
            self.update_counts()

            #card comparison:
            if deck1_card[1] > deck2_card[1]:
                self.interface.display_winner("deck1")
                self.deck1.append(deck2_card)
                self.deck1.append(deck1_card)
                self.update_counts()
            elif deck2_card[1] > deck1_card[1]:
                self.interface.display_winner("deck2")
                self.deck2.append(deck1_card)
                self.deck2.append(deck2_card)
                self.update_counts()
            else: #war
                self.interface.start_war()
                self.wartime(deck1_card,deck2_card)
        if self.deck1.cardsLeft() != 0:
            self.interface.winner_is("deck1")
        else:
            self.interface.winner_is("deck2")

    def wartime(self,card1,card2):
        deckpile = [card1,card2]
        a = 0
        b = 0
        while True:
            for i in  range(2):
                try:
                    if i == 0:
                        a = self.deck1.dealCard()
                        b = self.deck2.dealCard()
                        self.interface.draw_war_cards_down(a, b)
                        deckpile.extend([a,b])
                        self.update_counts()
                    elif i == 1:
                        a = self.deck1.dealCard()
                        b = self.deck2.dealCard()
                        self.interface.draw_war_cards_up(a, b)
                        deckpile.extend([a,b])
                        self.update_counts()
                except IndexError:
                    if self.deck1.cardsLeft() == 0:
                        self.interface.war_nocards("deck1")
                        for card in deckpile:
                            self.deck2.append(card)
                        self.update_counts()
                        return
                    else:
                        for card in deckpile:
                            self.deck1.append(card)
                        self.interface.war_nocards("deck2")
                        self.update_counts()
                        return
            if a[1] > b[1]:
                self.interface.display_war_winner("deck1")
                for card in deckpile:
                    self.deck1.append(card)
                self.update_counts()
                return
            elif a[1] < b[1]:
                self.interface.display_war_winner("deck2")
                for card in deckpile:
                    self.deck2.append(card)
                self.update_counts()
                return


class Interface:

    def __init__(self):
        self.win = GraphWin("War", 1000, 900)
        self.win.setBackground("darkgreen")
        self.status = Text(Point(500, 50), "")
        self.status.setSize(16)
        self.status.setTextColor("white")
        self.status.draw(self.win)

        label1 = Text(Point(250, 800), "Deck 1")
        label1.setTextColor("white")
        label1.draw(self.win)
        self.cards1 = Text(Point(250, 780), "")
        self.cards1.setTextColor("white")
        self.cards1.draw(self.win)

        label2 = Text(Point(750, 800), "Deck 2")
        label2.setTextColor("white")
        label2.draw(self.win)
        self.cards2 = Text(Point(750, 780), "")
        self.cards2.setTextColor("white")
        self.cards2.draw(self.win)

        # counts pairs dealt in the current war to determine the
        # coordinate set to use so a repeated tie during the same war
        # doesn't draw over the previous pair's cards
        self.war_round = 0

        # This is for undrawing everything after war ends
        self.war_cards_drawn = []

        # normal round position stays center 
        self.normal_pos1 = Point(250, 450)
        self.normal_pos2 = Point(750, 450)

        # 1st war pair: left/right of the initial card
        # layout left-to-right: [faceup] [initial] [facedown]
        self.war_up_pos1 = Point(130, 450)
        self.war_up_pos2 = Point(630, 450)
        self.war_down_pos1 = Point(370, 450)
        self.war_down_pos2 = Point(870, 450)

        # 2nd war pair (cards 3 & 4, if war triggers again in the same war):
        # same left/right layout, shifted to its own row
        #I have literally never seen a 2nd war pair in testing
        self.war_up_pos1_alt = Point(130, 600)
        self.war_up_pos2_alt = Point(630, 600)
        self.war_down_pos1_alt = Point(370, 600)
        self.war_down_pos2_alt = Point(870, 600)

    def update_deck_counts(self, deck1_count, deck2_count):
        self.cards1.setText(str(deck1_count))
        self.cards2.setText(str(deck2_count))

    def card_filename(self,card):
        suit, rank = card
        if rank == 1:
            rank_str = "ace"
        elif rank == 11:
            rank_str = "jack"
        elif rank == 12:
            rank_str = "queen"
        elif rank == 13:
            rank_str = "king"
        else:
            rank_str = str(rank)
        return f"Ex 7/{rank_str}_of_{suit.lower()}.png"

    def positions(self, kind):

        if kind == "normal":
            return self.normal_pos1, self.normal_pos2
        use_alt = (self.war_round % 2 == 0)
        if kind == "right":
            return (self.war_down_pos1_alt, self.war_down_pos2_alt) if use_alt else (self.war_down_pos1, self.war_down_pos2)
        else: #left
            return (self.war_up_pos1_alt, self.war_up_pos2_alt) if use_alt else (self.war_up_pos1, self.war_up_pos2)

    def clear_war_cards(self):
        for obj in self.war_cards_drawn:
            obj.undraw()
        self.war_cards_drawn = []

    def show_card(self, slot, card, kind="normal"):
        pos1, pos2 = self.positions(kind)
        pos = pos1 if slot == 1 else pos2
        img = Image(pos, self.card_filename(card))
        img.draw(self.win)
        if kind != "normal":
            self.war_cards_drawn.append(img)

    def show_facedown(self, slot, kind="right"):
        pos1, pos2 = self.positions(kind)
        pos = pos1 if slot == 1 else pos2
        back = Rectangle(Point(pos.x - 50, pos.y - 72), Point(pos.x + 50, pos.y + 72))
        back.setFill("gray")
        back.draw(self.win)
        if kind != "normal":
            self.war_cards_drawn.append(back)

    def drawing_cards(self, card1, card2):
        self.show_card(1, card1, "normal")
        self.show_card(2, card2, "normal")
        self.status.setText("Dealing..." + "\n Press again to continue.")
        self.win.getMouse()

    def display_winner(self, who):
        self.status.setText(f"{who} wins the round" + "\n Press again to continue.")
        self.win.getMouse()

    def start_war(self):
        self.war_round = 0
        self.clear_war_cards()
        self.status.setText("WAR!" + "\n Press again to continue.")
        self.win.getMouse()

    def draw_war_cards_down(self, card1, card2):
        self.war_round += 1
        self.show_facedown(1, "right")
        self.show_facedown(2, "right")
        self.status.setText("Placing war cards..." + "\n Press again to continue.")
        self.win.getMouse()

    def draw_war_cards_up(self, card1, card2):
        self.show_card(1, card1, "left")
        self.show_card(2, card2, "left")
        self.status.setText("Revealing..." + "\n Press again to continue.")
        self.win.getMouse()

    def display_war_winner(self, who):
        self.status.setText(f"{who} wins the war" + "\n Press again to continue.")
        self.win.getMouse()
        self.clear_war_cards()

    def war_nocards(self, who):
        self.status.setText(f"{who} ran out of cards during war" + "\n Press again to continue.")
        self.win.getMouse()
        self.clear_war_cards()

    def winner_is(self, who):
        self.status.setText(f"GAME OVER - {who} wins")
        self.win.getMouse()


interface = Interface()
game = model(interface)
game.run()
