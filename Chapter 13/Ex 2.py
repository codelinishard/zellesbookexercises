#reading the print statements are terrible
class FibCounter:
    def __init__(self):
        self.count = 0

    def getCount(self):
        return self.count
    def resetCount(self):
        self.count = 0

    def fib(self,n, depth=0):
        indent = "   " * depth
        print(f"{indent}computing fib({n})")
        self.count += 1
        
        if n < 3:
            print(f"{indent}Leaving fib({n}) returning 1")
            return 1
        else:
            output = self.fib(n-1, depth+1) + self.fib(n-2, depth+1)
            print(f"{indent}Leaving fib({n}) returning {output}")
            return output

    def main(self):
        n = int(input("Which fibonacci number do you want to find? Type the int value: "))
        self.fib(n)
        print(f"fib(n) was called {self.count} times in total.")

a = FibCounter()
a.main()