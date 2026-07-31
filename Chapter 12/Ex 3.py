class model:

    def __init__(self,filename):
        self.filename = filename
        self.namelist = dict()
        filename = open(self.filename,"r")
        for line in filename:
            name, company, state, email = line.strip("\n").split(",")
            self.namelist[name] = {"company": company, "state": state, "email": email}
        filename.close()

    def addNew(self,name,company,state,email):
        self.namelist[name] = {"company": company, "state": state, "email": email}
        self.updateFile()

    def deleteName(self,name):
        del self.namelist[name]
        self.updateFile()

    def giveInfo(self,name):
        if name not in self.namelist:
            return "" #deliberate blank
        return self.namelist[name]
    
    def listNameAddress(self):
        nameAddress = []
        for name, info in self.namelist.items():
            nameAddress.append((name, info['email']))
        return nameAddress #gives name, email

    def searchByState(self,state:str):
        matchedNames = []
        for name, info in self.namelist.items():
            if info['state'] == state:
                matchedNames.append((name, info['email']))
        return matchedNames #gives names and email of people from that state
    
    def updateFile(self):
        filename = open(self.filename,"w")
        for name, info in self.namelist.items():
            filename.write(f"{name},{info['company']},{info['state']},{info['email']}\n")
        filename.close()
    
class view():
    def __init__(self,filename):
        self.printIntro()
        input1 = input()
        while input1 != "start" and input1 != "exit":
            print("Invalid input, please enter 'start' or 'exit'.")
            input1 = input()
            if input1 == "exit":
                print("Exiting program. Goodbye!")
                return
        self.modelside = model(filename)
        self.getInput()
    
    def getInput(self):
        input1 = ""
        while input1 != "exit":
            input1 = input("What would you like to do? (type 'help' for options): ").lower()
            if input1 == "help":
                self.helpPrompt()

            elif input1 == "add":
                name = input("Enter name: ")
                company = input("Enter company: ")
                state = input("Enter state: ")
                email = input("Enter email: ")
                self.modelside.addNew(name, company, state, email)
                print(f"{name} has been added to the database.")

            elif input1 == "delete":
                name = input("Enter name (case sensitive): ")
                self.modelside.deleteName(name)
                print(f"{name} has been deleted from the database.")

            elif input1 == "search":
                name = input("Enter name (case sensitive): ")
                info = self.modelside.giveInfo(name)
                if info == "":
                    print("Name not found in database.")
                else: 
                    print(f"Name: {name}, Company: {info['company']}, State: {info['state']}, Email: {info['email']}")

            elif input1 == "list":
                Entirelist = self.modelside.listNameAddress()
                for name, email in Entirelist:
                    print(f"Name: {name}, Email: {email}")

            elif input1 == "searchbystate":
                state = input("Enter state: ").capitalize()
                matchedNames = self.modelside.searchByState(state)
                if matchedNames:
                    print(f"Names from {state} with their email:")
                    for name, email in matchedNames:
                        print(f"Name: {name}, Email: {email}")
                else:
                    print(f"No names found from {state}.")
            elif input1 == "exit":
                print("Exiting program. Goodbye!")
                return
            else:
                print("Invalid input, please try again.")

    def helpPrompt(self):
        print("To add a name, type 'add'. To delete a name, type 'delete'.")
        print("To search for a name, type 'search'. To list all names and email addresses, type 'list'.")
        print("To search for names by state, type 'searchbystate'. To exit, type 'exit'.")
    
    def printIntro(self):
        print("Welcome to the Conference Database!")
        print("You can add, delete, and search for names in the database.")
        print("You can also list all names and their email addresses.")
        print("You can also search for addresses of all people from a certain state.")
        print("To get started, type 'start'. To exit, type 'exit'.")


view1 = view("Ex 3.txt")