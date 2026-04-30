# I couldn't reuse much from Chap 9 Ex 12. The scope of the programme was too different
import random

class SideWalk:
    def __init__(self,n):
        self.n = n
        self.pathDict = {}
        for i in range(0,n+1):
            self.pathDict[i] = 0
        self.currentPos = n//2 #middle position of sidewalk length n

    def getSteps(self,key):
        return self.pathDict[key]
    def updatePos(self,change):
        self.currentPos += change
    def updateDict(self):
        self.pathDict[self.currentPos] = self.pathDict[self.currentPos] + 1
    

def main():
    n = int(input("Enter the length of the sidewalk: "))
    t = int(input("Enter the number of trials to simulate: "))
    avgSteps = simulateTrials(t,n)
    printSummary(t,n,avgSteps)

def simulateSteps(x):
    sidewalk = SideWalk(x)
    while sidewalk.currentPos != 0 and sidewalk.currentPos != x:
        step = random.choice([-1, 1])
        sidewalk.updatePos(step)
        sidewalk.updateDict()
    stepSum = []
    for i in range(x+1): #converts dict to a list
        stepSum.append(sidewalk.getSteps(i))
    return stepSum

def simulateTrials(t,n):
    average = [0] * (n+1)
    for i in range(t):
        h = simulateSteps(n)
        for x in range(n+1):
            average[x] += h[x] 
    for i in range(len(average)):        
        average[i] = average[i]/t

    return average

def printSummary(t,n,avgSteps):
    print(f"In {t} trials for sidewalks of length {n} units, the number of steps")
    print(f"for each tile are as follows.")
    for step in range(len(avgSteps)):
        if step == 0:
            print(f"The starting square was stepped on average {avgSteps[step]:.1f} times")
        if step == n:
            print(f"The ending square was stepped on average {avgSteps[step]:.1f} times")
        else: print(f"Square {step} was stepped on average {avgSteps[step]:.1f} times")
    

main()