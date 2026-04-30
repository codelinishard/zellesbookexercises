def innerProd(x,y):
	length = len(x)
	total = 0
	for i in range(length):
		sum += x[i] * y[i]
	return total

def main():
	x = [1, 2, 3, 4]
	y = [5, 6, 7, 8]
	total = innerProd(x,y)
	print(total)