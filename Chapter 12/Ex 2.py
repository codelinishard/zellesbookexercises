from random import random
class model:
    def __init__(self,interface,Asuccess,Bsuccess,serving,reportFrequency):
        self.interface = interface
        self.Asuccess = Asuccess
        self.Bsuccess = Bsuccess
        self.scoreA = 0
        self.scoreB = 0
        self.iterations = 0
        self.reportFrequency = reportFrequency
        self.serving = serving
        self.Awins = 0
        self.Bwins = 0
        self.wantContinue = True
    
    def run(self):
        while self.wantContinue == True:
            self.scoreA = 0
            self.scoreB = 0
            while not self.gameOver(self.scoreA,self.scoreB):
                self.simOneRally()

            self.tabulateResults()
            self.iterations = self.iterations + 1
            if self.iterations % self.reportFrequency == 0:
                self.interface.results(self.Awins,self.Bwins,self.iterations)
                self.wantContinue = self.wantToContinue()
        self.interface.endresults(self.Awins,self.Bwins,self.iterations)



    def wantToContinue(self):
        return self.interface.askcontinue()

    def tabulateResults(self):
        if self.scoreA > self.scoreB:
            self.Awins = self.Awins + 1
        else:
            self.Bwins = self.Bwins + 1

    def gameOver(self,scoreA,scoreB):
        return (scoreA >= 25 and scoreA - scoreB >= 2) or (scoreB >= 25 and scoreB - scoreA >= 2)
    
    def simOneRally(self):
        keepRallying = True
        service = self.serving
        while keepRallying:
            overNet = self.checkSuccess(service)
            if overNet: 
                if service == "A":
                    service = "B"
                else:
                    service = "A"
            else:
                if service == "A":
                    self.scoreB = self.scoreB + 1
                    self.serving = "B"
                else:
                    self.scoreA = self.scoreA + 1
                    self.serving = "A"
                keepRallying = False
    
    def checkSuccess(self,service):
        if service == "A":
            return random() <= self.Asuccess
        else:
            return random() <= self.Bsuccess

class view:
    def __init__(self):
        print("Welcome to the Volleyball Simulator!")
        self.continueGame = True
        checkContinue = input("Would you like to play? (Y/N) ")
        while checkContinue not in ["Y","N"]:
            print("Invalid input, please enter Y or N.")
            checkContinue = input("Would you like to play? (Y/N) ")
        if checkContinue == "N":
            self.continueGame = False
            return
        else:
            self.Aname = input("Enter team A's name: ")
            self.Bname = input("Enter team B's name: ")
            self.Asuccess = float(input("Enter team A's success rate (0-1): "))
            self.Bsuccess = float(input("Enter team B's success rate (0-1): "))
            self.serving = input("Which team serves first? (A/B) ")
            self.reportFrequency = int(input("How many games should be played before reporting intermediate results? "))
    
    def passVariables(self):
        return self.Asuccess,self.Bsuccess,self.serving,self.reportFrequency

    def results(self,winsA,winsB,iterations):
        print(f"After {iterations} games, {self.Aname} has won {winsA} times and {self.Bname} has won {winsB} times.")
        
    def askcontinue(self):
        checkContinue = input("Would you like to continue iterating? (Y/N) ")
        while checkContinue not in ["Y","N"]:
            print("Invalid input, please enter Y or N.")
            checkContinue = input("Would you like to continue iterating? (Y/N) ")
        if checkContinue == "N":
            return False
        else:
            return True    

    def endresults(self,Awins,Bwins,iterations):
        print(f"After {iterations} games, {self.Aname} won {Awins} times and {self.Bname} won {Bwins} times. Thanks for playing!")
interface = view()
if interface.continueGame:
    Asuccess,Bsuccess,serving,reportFrequency = interface.passVariables()
    volleyball = model(interface,Asuccess,Bsuccess,serving,reportFrequency)
    volleyball.run()