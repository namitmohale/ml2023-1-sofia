import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from scipy.stats import linregress

class KNNRegressor:
    def __init__(self):
        self.inputPoints = np.empty((0, 2))
        self.k = 1
    
    def readPoints(self, n, k):
        self.k = k
        for i in range(n):
            x = float(input(f"Enter x value for Point {i + 1}: "))
            y = float(input(f"Enter y value for Point {i + 1}: "))
            self.inputPoints = np.append(self.inputPoints, [[x, y]], axis=0)

    def applyKNNAndPredit(self, inputX):
        # Prepare the input for kNN.
        X = self.inputPoints[:, 0].reshape(-1, 1)
        y = self.inputPoints[:, 1]

        knn_regressor = KNeighborsRegressor(n_neighbors=self.k)
        knn_regressor.fit(X, y)
        y_pred = knn_regressor.predict([[inputX]])[0]
        coeff = knn_regressor.score(X, y)

        return y_pred, coeff

if __name__ == "__main__":
    N = 0
    while N <= 0:
        N = int(input("Enter the number of points (N): "))
        if N <= 0:
            print("N must be a positive integer.")
    
    k = 0
    while k <= 0 or k > N:
        k = int(input("Enter number of neighbors for kNN (k): "))
        if k <= 0 or k > N:
            print("k must be a positive integer <= N")
    
    knnRegressor = KNNRegressor()
    knnRegressor.readPoints(N, k)

    inputX = float(input("Enter input X for prediction by kNN Regressor: "))

    yPredicted, coeff = knnRegressor.applyKNNAndPredit(inputX)

    print(f"Value of y predicted by kNN Regressor for input X ({inputX}): y_pred = {yPredicted}, coeffecient of determination = {coeff}")
