from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
import json



class ModelEvaluator:

    def evaluate(self, model, X_test, y_test):

        predictions = model.predict(X_test)

        probabilities = model.predict_proba(X_test)[:,1]

        metrics = {

            "accuracy": accuracy_score(y_test, predictions),

            "precision": precision_score(y_test, predictions),

            "recall": recall_score(y_test, predictions),

            "f1": f1_score(y_test, predictions),

            "roc_auc": roc_auc_score(y_test, probabilities)

        }

        return metrics
    


    def generate_report( self, results, save_path="reports/evaluation_report.json"):
        report = {}
        for model_name, info in results.items():
            report[model_name] = info["metrics"]
        with open(save_path, "w") as file:
            json.dump(
                report,
                file,
                indent=4
            )
        print("Evaluation report saved successfully.")   