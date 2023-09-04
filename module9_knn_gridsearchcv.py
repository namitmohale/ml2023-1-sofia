import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class GetKAndAccuracy():
    def __init__(self):
        self.TrainS = []
        self.TestS = []
    
    def getTrainingData(self):
        N = 0
        while N <= 0:
            N = int(input("Enter the number of points in training data (N): "))
            if N <= 0:
                print("N must be a positive integer. Try again.")
        for n in range(N):
            X = float(input(f"Enter X value for point {n+1} in training data: "))
            Y = -1
            while Y < 0:
                Y = int(input(f"Enter Y value for point {n+1} in training data: "))
                if Y < 0:
                    print("Y must be a non-negative integer. Try Again.")
            self.TrainS.append((X, Y))
    
    def getTestData(self):
        M = 0
        # For good performance, M must be less than N. But since this condition
        # is not a part of the assignment, I will not include it.
        while M <= 0:
            M = int(input("Enter the number of points in test data (M): "))
            if M <= 0:
                print("M must be a positive integer. Try again.")
        for m in range(M):
            X = float(input(f"Enter X value for point {m+1} in test data: "))
            Y = -1
            while Y < 0:
                Y = int(input(f"Enter Y value for point {m+1} in test data: "))
                if Y < 0:
                    print("Y must be a non-negative integer. Try Again.")
            self.TestS.append((X, Y))
    
    def applyKNN(self):
        maxAccuracy = 0
        optimalK = 0
        for k in range(1, 11):
            knn = KNeighborsClassifier(n_neighbors=k)
            trainingData = np.array(self.TrainS)
            X_train = trainingData[:, 0].reshape(-1, 1)
            y_train = trainingData[:, 1]
            knn.fit(X_train, y_train)

            testData = np.array(self.TestS)
            X_test = testData[:, 0].reshape(-1, 1)
            y = testData[:, 1]
            y_pred = knn.predict(X_test)

            accuracy = accuracy_score(y, y_pred)
            if accuracy > maxAccuracy:
                maxAccuracy = accuracy
                optimalK = k
        return optimalK, maxAccuracy

if __name__ == "__main__":
    getKAndAccuracy = GetKAndAccuracy()
    getKAndAccuracy.getTrainingData()
    getKAndAccuracy.getTestData()
    k, accuracy = getKAndAccuracy.applyKNN()
    print(f"The optimal k for kNN on given data is {k} with an accuracy of {accuracy}")
