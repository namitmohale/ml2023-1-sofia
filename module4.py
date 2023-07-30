def findIndex(inputNumbers, target):
    for i in range(inputNumbers):
        if inputNumbers[i] == target:
            return i + 1
    return -1

def main():
    N = 0
    while N <= 0:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            print("N must be a positive integer.")
    inputNumbers = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        inputNumbers.append(num)
    X = int(input("Enter the number to search (X): "))

    idx = findIndex(inputNumbers, X)

    if idx == -1:
        print("-1")
    else:
        print(f"The index of {X} is: {idx}")

if __name__ == "__main__":
    main()
