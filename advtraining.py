import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
dataset = pd.read_csv("Advertising.csv")
x=dataset[["TV","Radio"]]
y=dataset[["Sales"]]
model = LinearRegression()
model.fit(x,y)
joblib.dump(model,"advtrain-model.pkl")