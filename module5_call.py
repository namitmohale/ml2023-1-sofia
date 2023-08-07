from module5_mod import NumberFinder

def main():
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

if __name__ == "__main__":
    main()