import yaml
import joblib
import pandas as pd
from trainer import ModelTrainer
from evaluator import ModelEvaluator
from model_selection import ModelSelector
from src.utils.config import ConfigManager

config_manager = ConfigManager()
config = config_manager.get()

test_df = pd.read_csv(config["data"]["processed_test_path"])
x_test = test_df.drop(columns=["Class"], axis = 1)
y_test = test_df["Class"]

trainer = ModelTrainer()
evaluator = ModelEvaluator()
selector = ModelSelector()

lr = trainer.train_logistic()
rf = trainer.random_forest()
xgb = trainer.xgboost()

results = {}

results["Logistic Regression"] = {
    "model": lr,
    "metrics": evaluator.evaluate(
        lr,
        x_test,
        y_test
    )
}

results["Random Forest"] = {
    "model": rf,
    "metrics": evaluator.evaluate(
        rf,
        x_test,
        y_test
    )
}
results["XGBoost"] = {
    "model": xgb,
    "metrics": evaluator.evaluate(
        xgb,
        x_test,
        y_test
    )
}



name, model, score = selector.select_best(results)

print(f"Best Model : {name}")

print(f"Best F1 : {score}")


joblib.dump(
    model,
    config["artifacts"]["best_model"]
)

print("Best model saved.")