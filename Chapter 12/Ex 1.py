# guipoker.py

from graphics import *
# from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView
from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10:
            outcome = self.interface.wantToPlay()
            if outcome == "Roll Dice":
                self.playRound()
            elif outcome == "Help":
                self.interface.helpInfo()
            elif outcome == "Quit":
                #check if top 10
                if self.isTop10(self.money):
                    name = self.interface.getName() #request name
                    self.editScoreList(name,self.money) #add name
                self.interface.close()
                return
        
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)        

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()
    def isTop10(self,currentScore): 
        filelist = open("Ex 1.txt","r")
        self.scores = []
        for line in filelist:
            name,score = line.strip("\n").split()
            score = int(score)
            self.scores.append([name,score])
        if self.scores == []:
            filelist.close()
            return True
        filelist.close()
        if currentScore > min(self.scores, key = lambda x: x[1])[1]:
                return True
    def editScoreList(self,name,currentScore):
        filelist = open("Ex 1.txt","r")
        self.scores = []
        for line in filelist:
            name,score = line.strip("\n").split()
            score = int(score)
            self.scores.append([name,score])
        filelist.close()
        self.scores.append([name,currentScore])
        self.scores.sort(key = lambda x: x[1], reverse = True)
        self.scores = self.scores[:10] #removes 11th entry
        filelist = open("top10score.txt","w")
        for i in range(len(self.scores)):
            filelist.write(f"{self.scores[i][0]} {self.scores[i][1]}\n")
        filelist.close()

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        close = Button(self.win,Point(300,230),400,40,"Exit")
        open_prompt = Button(self.win,Point(300,376),450,50,"Let's Play!")
        self.buttons = [close,open_prompt]
        self.closewin = False
        while True:
            b = self.choose(["Exit","Let's Play!"])
            if b == "Exit":
                self.win.close()
                self.closewin = True
                return
            elif b == "Let's Play!":
                self.setup()
                return
        
    def setup(self):
        self.createDice(Point(300,100), 75)
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        b = Button(self.win, Point(570,325), 40, 30, "Help")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit", "Help"])
        self.msg.setText("")
        return ans

    def close(self):
        self.win.close()

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []                   # No dice chosen yet
        while True: 
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score","Help"])

            if b[0] == "D":            # User clicked a die button
                i = eval(b[4]) - 1     # Translate label to die index
                if i in choices:       # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:                  # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            elif b == "Help":
                self.helpInfo()
            else:                      # User clicked Roll or Score
                for d in self.dice:    # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":       # Score clicked, ignore choices
                    return []
                elif choices != []:    # Don't accept Roll unless some
                    return choices     #   dice are actually selected

    
    def choose(self, choices):
        buttons = self.buttons
        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.

    def helpInfo(self): # I give up making them aligned, it might be a guess and check hardcoding
        helpWin = GraphWin("Help info", 400, 400)
        helpWin.setBackground("green3")
        helpClose = Button(helpWin, Point(200,20), 50, 50, "Close")
        helpClose.activate()
        line1 = Text(Point(200,100), """Player starts with $100 and each round costs $10
to play. This amount is subtracted at the start of
each round. The initial roll is a random hand. Two
chances are given to enhance the hand via rerolls 
every round. At the end, your money is updated    
according to the payout schedule below.           """)
        row1 = 'pay'
        row2 = '$5 '
        row3 = '$8 '
        row4 = '$12'
        row5 = '$15'
        row6 = '$20'
        row7 = '$30'
        row8 = 'hand'
        row9 = 'Two Pairs'
        row10 = 'Three of a kind'
        row11= 'Full house(Pair + Three of a kind)'
        row12 = 'Four of a kind'
        row13 = 'Straight (1-5 or 2-6)'
        row14 = 'Five of a kind'
        payoutlist = [row1,row2,row3,row4,row5,row6,row7]
        rowX = 350
        rowY = 200
        for row in payoutlist:
            Texts = Text(Point(rowX,rowY),row)
            Texts.draw(helpWin)
            rowY += 25
        combolist = [row8,row9,row10,row11,row12,row13,row14]
        rowX = 120
        rowY = 200
        for row in combolist:
            Texts = Text(Point(rowX, rowY),row)
            rowY +=25
            Texts.draw(helpWin)
        line1.draw(helpWin)
        
        while True:
            click = helpWin.getMouse()
            if helpClose.clicked(click):
                helpWin.close()
                return
    def getName(self):
        nameWin = GraphWin("Enter Name", 480, 200)
        nameWin.setBackground("green3")
        prompt = Text(Point(240,50), "Congratulations! You made the top 10! Please enter your name:")
        prompt.draw(nameWin)
        entry = Entry(Point(200,100), 20)
        entry.draw(nameWin)
        submit = Button(nameWin, Point(200,150), 50, 30, "Submit")
        submit.activate()
        while True:
            click = nameWin.getMouse()
            if submit.clicked(click):
                name = entry.getText()
                if name == "":
                    name = "Anonymous"
                nameWin.close()
                return name
        

inter = GraphicsInterface()
if inter.closewin == False:
    app = PokerApp(inter)
    app.run()

