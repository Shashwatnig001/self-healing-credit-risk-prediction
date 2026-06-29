import json

from ydata_profiling import report

def create_validation_report(
    schema_valid,
    missing_values,
    duplicates,
    negative_amounts,
    class_distribution
    ):

    report = {

        "schema_valid": schema_valid,

        "missing_values": int(missing_values),

        "duplicates": int(duplicates),

        "negative_amounts": int(negative_amounts),

        "class_distribution": class_distribution

    }

    return report


def save_report(report, path="reports/validation_report.json"):

    with open(path, "w") as file:

        json.dump(report, file, indent=4)

    print("Validation report saved successfully.")