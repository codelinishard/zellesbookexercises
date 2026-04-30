class Set:
    def __init__(self,elements):
        self.elements = elements
    def addElement(self,x):
        self.elements.append(x)
    def deleteElement(self,x):
        if x in self.elements:
            self.elements.remove(x)
    def member(self,x):
        if x in self.elements:
            return True
        else:
            return False
    def intersection(self,set2):
        commons = []
        for n in set2:
            if n in self.elements:
                commons.append(n)
        return Set(commons)
    def union(self,set2):
        unified = []
        for n in set2:
            if n not in unified:
                unified.append(n)
        for n in self.elements:
            if n not in unified:
                unified.append(n)
        unified.sort()
        return Set(unified)
    def subtract(self,set2):
        new = []
        for n in self.elements:
            if n not in set2:
                new.append(n)
        return Set(new)