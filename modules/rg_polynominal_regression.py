import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('../dataset/Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values  # grabbing all columns except last one (all independent variables)
y = dataset.iloc[:, -1].values  # values of the last column (all dependent variables)

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)


# Visualising the Polynominal Regression result
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg2.predict(X_poly), color='blue')  # we have to change argument of predict function on a matrix of NOT single feature
plt.title('Truth or bluff (Polynominal Linear Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()



