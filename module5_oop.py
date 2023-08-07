class NumberFinder:
    def __init__(self):
        self.inputNumbers = []

    def readNumbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.inputNumbers.append(num)
    
    def findIndex(self, target):
        for i in range(len(self.inputNumbers)):
            if self.inputNumbers[i] == target:
                return i + 1
        return -1


if __name__ == "__main__":
    N = 0
    while N <= 0:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            print("N must be a positive integer.")
    
    numberFinder = NumberFinder()
    numberFinder.readNumbers(N)

    X = int(input("Enter the number to search (X): "))

    idx = numberFinder.findIndex(X)

    if idx == -1:
        print("-1")
    else:
        print(f"The index of {X} is: {idx}")
