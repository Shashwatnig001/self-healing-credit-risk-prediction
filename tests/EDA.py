import pandas as pd

df= pd.read_csv("D:/Mr.Coder/data/raw/creditcard.csv")

df.info()
print(df["Class"].value_counts())
print(df["Class"].value_counts(normalize= True))

