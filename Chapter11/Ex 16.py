from math import sqrt
class StatSet:
    def __init__(self):
        self.statlist = []
        self.mean = 0
        self.median = 0
        self.stdDev = 0
        self.count = 0
    
    def addNumber(self,x):
        self.statlist.append(x)
    
    def getmean(self):
        if not self.statlist : #blank
            return 0
        else:
            accumulator = 0
            for i in self.statlist:
                accumulator += i
            self.mean = accumulator / len(self.statlist)
            return self.mean
    
    def getmedian(self):
        if not self.statlist : #blank
            return 0
        else:
            self.getcount()
            if self.count % 2 != 0: #odd number
                self.median = self.count // 2
                return self.median
            else:
                self.median = (self.statlist[self.count//2] + self.statlist[self.count//2 - 1])/2
                return self.median
    
    def getstdDev(self):
        sumDevSq = 0.0
        for num in self.statlist:
            dev = num - self.mean
            sumDevSq = sumDevSq + dev * dev
        self.getcount()
        return sqrt(sumDevSq/(self.count-1))
    
    def getcount(self):
        self.count = len(self.statlist)
        return self.count
    
    def getmin(self):
        return min(self.statlist)
    def getmax(self):
        return max(self.statlist)


def getNumbers(data):
    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        data.addNumber(x)   # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
  
def main():
    print("This program computes mean, median and standard deviation.")
    data = StatSet()
    getNumbers(data)
    xbar = data.getmean()
    std = data.getstdDev()
    med = data.getmedian()
    
    print("\nThe mean is", xbar)
    print(f"The standard deviation is {std:.2f}")
    print("The median is", med)    

if __name__ == '__main__': main()