
import pandas as pd
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv("data.csv")
print(dataset)
x=dataset[["height"]]
y=dataset[["weight"]]
model= LinearRegression()
model.fit(x,y)
print("coefficient =", model.coef_)
print("intercept =", model.intercept_)

print(model.predict([[160]]))