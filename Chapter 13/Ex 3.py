def handle_input():
    string = input("\nType something to test if it is a palindrome. \n")
    string = string.lower()
    edited = ""
    for i in string:
        letter = i.strip(". , ; : ? ! '  - _ ( ) [ ] { } / ... —  @ # & * % ^ ~ ")
        edited = edited + letter  
    return edited

def incursion(string):
    if len(string) == 1: #odd number of letters
        return True
    elif string == "":#even number
        return True 

    if incursion(string[1:-1]):
        if string[0] == string[-1]:
            return True
    return False

def main():
    print("At any point, type 'end' to terminate. ")
    while True:
        string = handle_input()
        if string == "end":
            print("Terminated.")
            return
        if incursion(string):
            print("That is a palindrome.")
        else:
            print("That is not a palindrome.")

if __name__ == "__main__":
    main()
# A man, a plan, a canal, Panama
# Was it a car or a cat I saw?
# No lemon, no melon