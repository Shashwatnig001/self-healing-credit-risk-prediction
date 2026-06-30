import json
import yaml
from src.utils.config import ConfigManager


class DriftReport:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.config = self.config_manager.get()

    def generate_report(self, drift_results):
        report_path = self.config["reports"]["drift_report"]

        report = {
            "total_features": len(drift_results),
            "drifted_features": 0,
            "features": drift_results
        }
        for feature in drift_results:
            if drift_results[feature]["drift_detected"]:
                report["drifted_features"] += 1

        with open(report_path, "w") as file:
            json.dump(report, file, indent=4)

        print("Drift Report Generated Successfully.")

        