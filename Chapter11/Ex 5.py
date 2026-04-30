#myList.count(x)
def count(myList, x):
    accumulator = 0
    for term in myList:
        if term == x:
            accumulator += 1
    return accumulator
#x in myList
def isin(myList,x):
    for term in myList:
        if term == x:
            return True
    return False
#myList.index(x)
def index(myList,x):
    value = -1
    try: 
        for term in myList:
            value += 1
            if term == x:
                return value
    except: ValueError(f"{x} is not in the list")
#myList.reverse()
def reverse(myList):
    reversed = []
    for term in myList:
        reversed.insert(0,term)
    return reversed
#myList.sort()
def sort(mylist):
    alphabetOrder = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    sortedlist = []
    sortedlist.append(mylist[0])
    x = 1

    if isinstance(mylist[0], str): #check if sort by alphabetical
        for x in range(1,len(mylist)):
            word = mylist[x]
            wordno = alphabetOrder.index(mylist[x][0])
            i = 0
            try:
                while True:
                    indexno = alphabetOrder.index(sortedlist[i][0])
                    if wordno < indexno:
                        sortedlist.insert(i, word)
                        break
                    i += 1
            except IndexError: # i exceeds sortedlist range, meaning word has highest order
                sortedlist.append(word)
    else: # number sorting
        for x in range(1,len(mylist)):
            num = mylist[x]
            i = 0
            try:
                while True:
                    indexno = sortedlist[i]
                    if num < indexno:
                        sortedlist.insert(i,num)
                        break
                    i +=1
            except IndexError: # i exceeds sortedlist range, meaning num is largest
                sortedlist.append(num)
                
                    
                    

    
