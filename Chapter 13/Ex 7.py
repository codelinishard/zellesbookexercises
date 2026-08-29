from math import factorial
from time import perf_counter

def combination(n,k):
    return factorial(n)/((factorial(k) * factorial(n-k)))

def iterative(n,k):
    accumulator = 1
    for i in range(1, k+1):
        accumulator = accumulator * (n-i+1)/i
    return accumulator

def recursive(n,k):
    print(n) 
    #literally can't see if the program is still computing otherwise
    # if k is printed instead, it alternates 1 and 2
    if k > n:
        return 0
    elif k == 1: 
        # setting k == 0 as base case means recursive(n,1) will keep calling until n = 1. 
        # this is unncessary added recursive depth. since the amount of values from (1,n] is n,
        # there's a shortcut of returning n at k == 1
        return n
    elif k == n:
        return 1
    else:
        return recursive(n-1,k-1) + recursive(n-1,k)

def time_measurement(funct, n, k):
    start = perf_counter()
    funct(n,k)
    end = perf_counter()
    print(f"{end-start:g}")

time_measurement(recursive,20,10)
time_measurement(iterative,20,10)
time_measurement(combination,20,10)

#recursion is terrible, taking 7s on my computer, while iteration takes 0.00001s, and direct computing taking 0.0000045s