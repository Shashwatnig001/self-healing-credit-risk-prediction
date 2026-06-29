import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

class DataPreprocessor:

    def __init__(self):
        self.amount_scaler = StandardScaler()
        self.time_scaler = StandardScaler()

    def preprocess(self, df):
        df = df.copy();
        df.drop_duplicates(inplace=True)
        df['Amount'] = self.amount_scaler.fit_transform(df[['Amount']])
        df['Time'] = self.time_scaler.fit_transform(df[['Time']])
        return df
    
    def save_scaler(self):
        os.makedirs("models", exist_ok = True)
        joblib.dump(self.amount_scaler, "models/amount_scaler.pkl")
        joblib.dump(self.time_scaler, "models/time_scaler.pkl")


    def split_features_target(self,df):
        x = df.drop('Class', axis=1)
        y = df['Class']
        return x, y
    