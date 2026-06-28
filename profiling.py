import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("D:/Mr.Coder/data/raw/creditcard.csv")

profile = ProfileReport(df, title = "Credit Card Fraud", explorative = True)

profile.to_file("reports/EDA_Report.html")

print("EDA File created successfully")