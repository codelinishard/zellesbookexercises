from random import *

def dummy_list(oglist): 
    """Creates a list of equal length to list given. Values of each element is the position"""
    length = len(oglist)
    new_list = []
    for i in range(length):
        new_list.append(i)
    return new_list

def shuffle(myList):
    """Shuffles and returns a given list"""
    dummy = dummy_list(myList)
    final_list = []
    while len(final_list) < len(myList):
        no = randint(0,len(myList) - 1)
        if no in dummy:
            dummy.remove(no) 
            final_list.append(myList[no])
    return final_list
    
def main():
    toshuffle = [10, 23, 5, 17, 42, 8, 31, 6]
    print(toshuffle)
    nowshuffled = shuffle(toshuffle)
    print(nowshuffled)