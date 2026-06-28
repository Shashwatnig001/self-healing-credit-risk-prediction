import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, config_path = "configs/config.yaml"):

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)
        
    def load_data(self):
        path = self.config["data"]["raw_data_path"]
        df = pd.read_csv(path)
        print("Data Loaded successfully")
        print(f"shape: {df.shape}")
        return df
    
    def split_data(self):
        df = self.load_data()

        train_df , test_df = train_test_split(df, test_size=self.config["model"]["test_size"], random_state = self.config["model"]["random_state"], stratify = df["Class"])

        os.makedirs("data/processed", exist_ok = True)
        train_df.to_csv(self.config["data"]["train_path"], index = False)
        test_df.to_csv(self.config["data"]["test_path"], index = False)

        print("Train and Test saved successfully")

if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.split_data()



