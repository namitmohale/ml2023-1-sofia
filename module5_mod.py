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