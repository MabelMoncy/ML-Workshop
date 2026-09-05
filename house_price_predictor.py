import pandas as pd
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv("house_price_mlr_6point.csv")
print(dataset)
x = dataset[["Area_sqft_hundreds","Bedrooms"]]
y = dataset[["Price_Lakhs"]]
model = LinearRegression()
model.fit(x,y)
print(model.predict([[7, 3]]))