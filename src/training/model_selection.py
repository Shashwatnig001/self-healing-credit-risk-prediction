class ModelSelector:

    def select_best(self, results):

        best_model = None

        best_score = -1

        best_name = None

        for name, info in results.items():

            if info["metrics"]["f1"] > best_score:

                best_score = info["metrics"]["f1"]

                best_model = info["model"]

                best_name = name

        return best_name, best_model, best_score