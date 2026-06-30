import yaml
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from src.utils.config  import ConfigManager


class ModelTrainer:

    def __init__(self):
        self.config_manager = ConfigManager()
        self.config = self.config_manager.get()

    def load_data(self):
        path = self.config["data"]["processed_train_path"]
        df = pd.read_csv(path)

        x = df.drop(columns = ["Class"], axis = 1)
        y = df["Class"]
        return x, y
    
    def train_logistic(self):
        x,y = self.load_data()
        model = LogisticRegression(
            max_iter = self.config["training"]["models"]["logistic_regression"]["max_iter"],
            random_state = self.config["model"]["random_state"]
        )
        model.fit(x,y)
        return model
    
    def random_forest(self):
        x,y = self.load_data()
        model = RandomForestClassifier(
            n_estimator = self.config["training"]["models"]["random_forest"]["n_estimator"],
            random_state = self.config["model"]["random_state"]                                                                   
        )
        model.fit(x,y)
        return model
    
    def xgboost(self):
        x,y = self.load_data()
        model = XGBClassifier(
            n_estimator = self.config["training"]["models"]["xgboost"]["n_estimator"],
            random_state = self.config["model"]["random_state"]
        )
        model.fit(x,y)
        return model
    

