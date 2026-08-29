def baseConversion(num,base):
    if num < base:
        print(num, end = "")
    else:
        value = num % base #what will be printed
        remainder = num // base #thing passed into next recursion
        baseConversion(remainder, base)
        print("", value, end = "")



baseConversion(1234,16)