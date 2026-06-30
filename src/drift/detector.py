import yaml
import pandas as pd
from scipy.stats import ks_2samp
from src.utils.config import ConfigManager


class DriftDetector:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.config = self.config_manager.get()
        self.threshold = self.config["drift"]["threshold"]

    def load_data(self):
        reference_path = self.config["drift"]["reference_data_path"]
        current_path = self.config["drift"]["current_data_path"]
        reference_df = pd.read_csv(reference_path)
        current_df = pd.read_csv(current_path)
        return reference_df, current_df

    def detect_drift(self):
        reference_df, current_df = self.load_data()
        drift_results = {}
        features = reference_df.drop("Class", axis=1).columns
        for feature in features:
            statistic, p_value = ks_2samp(
                reference_df[feature],
                current_df[feature]
            )
            drift_results[feature] = {
                "ks_statistic": float(statistic),
                "p_value": float(p_value),
                "drift_detected": bool(p_value < self.threshold)
            }
        return drift_results