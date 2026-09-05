import pandas as pd
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv("study.csv")
x=dataset[["study_hours"]]
y=dataset[["mark_obtained"]]
model= LinearRegression()
model.fit(x,y)
print(dataset)
print("coefficient =", model.coef_)
print("intercept =", model.intercept_)
print(model.predict([[7]]))