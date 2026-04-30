# surprising amount of complexity for such a short program, took ages
def sieve(n):
	toSieve = listCreation(n)
	sieved = algoProcess(toSieve)
	return sieved

def listCreation(n):
	x = []
	for i in range(2,n+1):
		x.append(i)
	return x

def algoProcess(x):
    val = 0
    reducedList = []
    primelist = []
    while len(x)>0: #loop ends after final number is checked
        i = x[0]
        primelist.append(i)
        reducedList = checkOnePrime(x,i)
        x = reducedList.copy()

        
    return primelist

def checkOnePrime(x,prime):
    reducedList = []
    for y in range(len(x)):
        if x[y] % prime != 0:
            reducedList.append(x[y])
    return reducedList

def main():
	print("This function finds all the prime numbers up to the value you input.")
	n = int(input("Till what value do you want to check till(inclusive): "))
	final = sieve(n)
	print(f"The primes in the list starting 2 ending in {n} is ")
	print(final)
	
main()