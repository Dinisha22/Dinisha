# Example: Train a simple ML model to predict study hours -> exam score
from sklearn.linear_model import LinearRegression
import numpy as np

# Data: [hours studied], [exam score]
X = np.array([[1], [2], [3], [4], [5]])  # input
y = np.array([40, 50, 60, 70, 80])       # output

model = LinearRegression()
model.fit(X, y)  # training the model

print(model.predict([[5]]))  # predict score if studied 6 hrs