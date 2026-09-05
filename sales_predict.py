import joblib
model = joblib.load("advtrain-model.pkl")
input_tv = float(input("Enter TV budget: "))
input_radio = float(input("Enter Radio budget: "))
print(model.predict([[input_tv, input_radio]]))