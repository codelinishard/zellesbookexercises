# guipoker.py

from graphics import *
from button import *
#added undraw method for button, removed drawing button upon creation
class model:

    def __init__(self, filename):
        filelist = open(filename,"r")
        self.users = dict()
        for line in filelist:
            user, password, checkingAccount, savingsAccount = line.strip("\n").split()
            self.users[user] = [password, int(checkingAccount), int(savingsAccount)]
        filelist.close()

    def verify(self, userID, pin):
        if userID in self.users and self.users[userID][0] == pin:
            self.checkingAccount = self.users[userID][1]
            self.savingsAccount = self.users[userID][2]
            self.userID = userID
            return True
        else:
            return False

    def checkBalance(self):
        return self.checkingAccount, self.savingsAccount
    def checkChecking(self):
        return self.checkingAccount
    def checkSavings(self):
        return self.savingsAccount
    
    def withdraw(self, accountType, amount):
        amount = int(amount)
        if accountType == "Checking account":
            if amount > int(self.checkingAccount):
                return False, "no funds"
            else:
                self.checkingAccount = self.checkingAccount - amount
                return True, self.checkingAccount
        elif accountType == "Savings account":
            if amount > int(self.savingsAccount):
                return False, "no funds"
            else:
                self.savingsAccount = self.savingsAccount - amount
                return True, self.savingsAccount
        else:
            return False, "invalid account type"
        
    def transfer(self, fromAccount, toAccount, amount):
        amount = int(amount)
        if fromAccount == "checking" and toAccount == "savings":
            if amount > int(self.checkingAccount):
                return False, "no funds"
            else:
                self.checkingAccount = self.checkingAccount - amount
                self.savingsAccount = self.savingsAccount + amount
                return True, self.checkingAccount
        elif fromAccount == "savings" and toAccount == "checking":
            if amount > int(self.savingsAccount):
                return False, "no funds"
            else:
                self.savingsAccount = self.savingsAccount - amount
                self.checkingAccount = self.checkingAccount + amount
                return True, self.savingsAccount
        else:
            return False, "invalid account type"
        
    def updateFile(self,filename):
        filename = open(filename,"w")
        self.users[self.userID][1] = self.checkingAccount
        self.users[self.userID][2] = self.savingsAccount
        for user, info in self.users.items():
            filename.write(f"{user} {info[0]} {info[1]} {info[2]}\n")
        filename.close()
    

class GraphicsInterface:
    def __init__(self,model):
        self.win = GraphWin("ATM", 600, 400)
        self.model = model("Ex 4.txt")
        self.win.setBackground("white")
        banner = Text(Point(300,30), "ATM machine")
        banner.setSize(24)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(self.win)
        #msg, exit, and submit will be reused repeatedly
        self.submit = newButton(self.win,Point(300,350),100,60, "Submit")
        self.msg = Text(Point(300,70), "Enter your user ID and PIN to log in.")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.exitbutton = newButton(self.win,Point(540,370),100,40,"Exit")
        self.exitbutton.draw()
        open_prompt = newButton(self.win,Point(300,200),100,50,"Enter details")
        open_prompt.draw()
        self.buttons = []
        self.buttons.append(self.exitbutton)
        self.buttons.append(open_prompt)
        self.buttons.append(self.submit)
        self.closewin = False
        while True:
            b = self.choose(["Exit","Enter details"],self.buttons)
            if b == "Exit":
                self.win.close()
                self.closewin = True
                return
            elif b == "Enter details":
                self.exitbutton.undraw()
                open_prompt.undraw()

                self.msg.setText("")
                self.run()
                return

    def run(self):
        while True: #verify user validity
            userid,pin = self.getdetails()
            if userid is None and pin is None:
                return
            elif self.model.verify(userid,pin): #success
                break
            else:
                self.msg.setText("Incorrect details, press anywhere to try again.")
                self.win.getMouse()
                pass #restart cycle until correct
            
        self.setup()  
        while True:
            self.undrawsetup()
            self.drawmain4()
            self.msg.setText("What would you like to do today?")
            choice = self.choose(
            ["Withdraw cash", "Check balances", "Transfer money", "Exit"],
            self.buttons
            )
            if choice == "Check balances":
                checking, savings = self.model.checkBalance()
                self.undrawsetup()
                self.msg.setText(
                    "\n \n \n"
                    f"Your current checking account has {checking} dollars \n"
                    + f"Your current savings account has {savings} dollars \n"
                    + "Click anywhere to continue.")
                self.win.getMouse()
            elif choice == "Withdraw cash":
                self.withdrawProcess()
            elif choice == "Transfer money":
                self.transferProcess()
            elif choice == "Exit":
                self.msg.setText("Have a nice day. Click anywhere to close.")
                self.model.updateFile("Ex 4.txt")
                self.win.getMouse()
                self.close()
                return
                
    def transferProcess(self):
        self.undrawsetup()
        self.drawother3()
        self.msg.setText("Where do you want to transfer from?")
        choice = self.choose(["Checking account","Savings account"],self.checkingorsavings)
        if choice == "Checking account":
            self.savingsb.deactivate()
            self.msg.setText(
                "How much do you want to transfer? \n"
                + "Current balance is " + str(self.model.checkChecking())
                             )
        else:
            self.checkingb.deactivate()
            self.msg.setText(
                "How much do you want to transfer? \n"
                + "Current balance is " + str(self.model.checkSavings())
                )

        amtbox = Entry(Point(300,200),50)
        amtbox.draw(self.win)
        while True:
            self.choose(["Submit"],self.checkingorsavings)
            amt = amtbox.getText()
            try: 
                amt = int(amt) 
                break
            except ValueError:
                self.msg.setText("Invalid input. Click anywhere to try again.")
                self.win.getMouse()
            
        amtbox.undraw()
        if choice == "Checking account":
            outcome, result = self.model.transfer("checking","savings",amt)
        else:
            outcome, result = self.model.transfer("savings","checking",amt)
    
        if outcome == True:
            self.msg.setText("\n Successfully transferred $" + str(amt)
                             + "\n new balance is " + str(result)
                             + "\n Press anywhere to continue")
        elif outcome == False and result == "no funds":
            self.msg.setText("Withdrawal failed. Insufficient funds. \n"
                             + "Press anywhere to continue")
        self.win.getMouse()
                
                
    def withdrawProcess(self):
        self.undrawsetup()
        self.drawother3()
        self.msg.setText("Where do you want to withdraw from?")
        choice = self.choose(["Checking account","Savings account"],self.checkingorsavings)
        if choice == "Checking account":
            self.savingsb.deactivate()
            self.msg.setText(
                "How much do you want to withdraw? \n"
                + "Current balance is " + str(self.model.checkChecking())
                             )
        else:
            self.checkingb.deactivate()
            self.msg.setText(
                "How much do you want to withdraw? \n"
                + "Current balance is " + str(self.model.checkSavings())
                            )
        amtbox = Entry(Point(300,200),50)
        amtbox.draw(self.win)
        while True:
            self.choose(["Submit"],self.checkingorsavings)
            amt = amtbox.getText()
            try: 
                amt = int(amt) 
                break
            except ValueError:
                self.msg.setText("Invalid input. Click anywhere to try again.")
                self.win.getMouse()
            
        amtbox.undraw()
        outcome, result = self.model.withdraw(choice,amt)
        if outcome == True:
            self.msg.setText("\n Successfully withdrawn $" + str(amt)
                             + "\n new balance is " + str(result)
                             + "\n Press anywhere to continue")
        elif outcome == False and result == "no funds":
            self.msg.setText("Withdrawal failed. Insufficient funds. \n"
                             + "Press anywhere to continue")
        self.win.getMouse()
        
            
        
    def getdetails(self):
        self.msg.setText("Enter your userID and PIN")
        userIDbox = Entry(Point(300,200),50)
        userIDbox.setText("userID")
        userIDbox.draw(self.win)
        PINbox = Entry(Point(300,300),50)
        PINbox.setText("PIN")
        PINbox.draw(self.win)
        self.exitbutton.draw()
        self.submit.draw()
        decision = self.choose(["Exit","Submit"], self.buttons)
        if decision == "Exit":
            self.msg.setText("Closing program. Press again to exit.")
            self.win.getMouse()
            self.close()
            return None, None
            
            
        userID = userIDbox.getText()
        PIN = PINbox.getText()
        userIDbox.undraw()
        PINbox.undraw()
        self.submit.undraw()
        self.exitbutton.undraw()
        return userID,PIN

    def setup(self):
        self.buttons = [] #clearing unused buttons
        b = newButton(self.win, Point(100, 150), 200, 80, "Withdraw cash")
        self.buttons.append(b)
        b = newButton(self.win, Point(100, 350), 200, 80, "Check balances")
        self.buttons.append(b)
        b = newButton(self.win, Point(500,150),200,80, "Transfer money")
        self.buttons.append(b)
        b = newButton(self.win, Point(500,350),200,80, "Exit")
        self.buttons.append(b)
        
        self.checkingorsavings = []
        self.checkingb = newButton(self.win, Point(450,300),200,80, "Checking account")
        self.checkingorsavings.append(self.checkingb)
        self.savingsb = newButton(self.win, Point(150,300),200,80, "Savings account")
        self.checkingorsavings.append(self.savingsb)
        self.submitb = newButton(self.win, Point(300,350),100,80, "Submit")
        self.checkingorsavings.append(self.submitb)
        
        

    def undrawsetup(self):
        for button in self.buttons:
            button.undraw()
        for button in self.checkingorsavings:
            button.undraw()       
    def drawmain4(self):
        for button in self.buttons:
            button.draw()
    def drawother3(self):
        for button in self.checkingorsavings:
            button.draw()
            
    def close(self):
        self.model.updateFile("Banking details.txt")
        self.win.close()
    
    def choose(self, choices, buttonlist):
        if buttonlist == self.buttons:
            buttons = self.buttons
        elif buttonlist == self.checkingorsavings:
            buttons = self.checkingorsavings
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

class newButton(Button):

    """Added undraw, draw, and button does not draw upon initiation"""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        self.win = win
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.label = Text(center, label)

    def undraw(self):
        "Undraws the button entirely"
        self.rect.undraw()
        self.label.undraw()
    def draw(self):
        "Redraws the button entirely"
        self.rect.draw(self.win)
        self.label.draw(self.win)
        
interface = GraphicsInterface(model)


