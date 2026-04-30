def removeDuplicates(somelist):
    i = 0
    new_list = []
    dupe_list = []
    for i in range(len(somelist)):
        if somelist[i] not in new_list:
            new_list.append(somelist[i])
        elif somelist[i] in new_list:
            dupe_list.append(somelist[i])
    if len(new_list) == len(somelist):
        print("There are no duplicates")
    else: print(f"Duplicates {dupe_list} were removed")
    return new_list        

def main():
    test = [1, 2, 3, 2, 4, 1, 5, 3, 3]
    ntest = removeDuplicates(test)
    print(ntest)

main()