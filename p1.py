import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/Iris.csv")
print(data)
print(data.head(5))
print(data.tail(5))
print(data["SepalLengthCm"])
print(data.describe())
print(data["PetalLengthCm"])
print(data.info())
print(data.dtypes)
print(data.count())

