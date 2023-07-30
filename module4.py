def findIndex(inputNumbers, target):
    # We loop over all the user provided N numbers and if we find the target number,
    # we output index+1 (since indexes in computers start from 0 whereas we want them to start from 1),
    # or we return -1 if we cannot find the target number.
    for i in range(inputNumbers):
        if inputNumbers[i] == target:
            return i + 1
    return -1

def main():
    N = 0
    # Using a while loop to keep prompting the user until they input a valid value for N.
    while N <= 0:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            print("N must be a positive integer.")
    
    # inputNumbers will hold the N numbers provided by the user.
    inputNumbers = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        inputNumbers.append(num)

    # X is the number that we need to find among the numbers provided by the user.
    X = int(input("Enter the number to search (X): "))

    # idx holds the final result.
    idx = findIndex(inputNumbers, X)

    if idx == -1:
        print("-1")
    else:
        print(f"The index of {X} is: {idx}")

if __name__ == "__main__":
    main()
