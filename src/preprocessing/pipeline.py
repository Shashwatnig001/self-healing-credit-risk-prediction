from src.preprocessing.preprocess import DataPreprocessor
import pandas as pd
from src.utils.config import ConfigManager

config = ConfigManager().get()

train_path = config["data"]["train_path"]
df = pd.read_csv(train_path)

processor = DataPreprocessor()

df = processor.preprocess(df)

x , y = processor.split_features_target(df)

processor.save_scalers()

print(x.shape)

print(y.shape)

processed_train_path = config["data"]["processed_train_path"]

df.to_csv(processed_train_path, index=False)

print("Processed training data saved successfully.")