from detector import DriftDetector
from report import DriftReport


class DriftPipeline:
    def __init__(self):
        self.detector = DriftDetector()
        self.report = DriftReport()

    def run(self):
        print("="*60)
        print("DRIFT DETECTION PIPELINE STARTED")
        print("="*60)
        drift_results = self.detector.detect_drift()
        self.report.generate_report(drift_results)
        print("="*60)
        print("DRIFT DETECTION COMPLETED")
        print("="*60)
        
if __name__ == "__main__":
    pipeline = DriftPipeline()
    pipeline.run()