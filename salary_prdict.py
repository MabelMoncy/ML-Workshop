import joblib
model = joblib.load("bigdata_model.pkl")
input = int(input("Enter years of experience: "))
print(model.predict([[input]]))