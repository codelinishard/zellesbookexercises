def baseConversion(num):
    translator = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    if num <= 9:
        print(translator[num], end = "")
    else:
        value = num % 10 #what will be printed
        remainder = num // 10 #thing passed into next recursion

        baseConversion(remainder)
        print("", translator[value], end = "")



baseConversion(1234)