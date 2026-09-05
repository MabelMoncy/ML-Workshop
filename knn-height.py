import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
dataset = pd.read_csv("data.csv")
print(dataset)
x= dataset[["height"]]
y= dataset[["weight"]]
model = KNeighborsRegressor(n_neighbors=3)
model.fit(x,y)
print(model.predict([[160]]))