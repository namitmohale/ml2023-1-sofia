import numpy as np
from sklearn.metrics import precision_score, recall_score

class PrecisionAndRecall:
    def __init__(self, N):
        self.N = N
        self.groundTruth = np.zeros(N, dtype=int)
        self.prediction = np.zeros(N, dtype=int)
    
    def DataInitializer(self):
        for i in range(self.N):
            x = -1
            while x != 0 and x != 1:
                x = int(input(f"Enter X (Ground Truth) value for point {i+1}: "))
                if x != 0 and x != 1:
                    print("Value of X should be 0 or 1. Try Again.")
            self.groundTruth[i] = x

            y = -1
            while y != 0 and y != 1:
                y = int(input(f"Enter y (Prediction) value for point {i+1}: "))
                if y != 0 and y != 1:
                    print("Value of y should be 0 or 1. Try Again.")
            self.prediction[i] = y
    
    def CalculatePrecisionAndRecall(self):
        precision = precision_score(self.groundTruth, self.prediction)
        recall = recall_score(self.groundTruth, self.prediction)
        return precision, recall

if __name__ == "__main__":
    N = 0
    while N <= 0:
        N = int(input("Enter the number of points (N): "))
        if N <= 0:
            print("N must be a positive integer. Try again.")
    
    precisionAndRecall = PrecisionAndRecall(N)
    precisionAndRecall.DataInitializer()
    precision, recall = precisionAndRecall.CalculatePrecisionAndRecall()

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")