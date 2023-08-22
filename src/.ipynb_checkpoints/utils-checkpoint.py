import pandas as pd
#Fonction pour filtrer suivant le MIN_COMPLETION_RATE
def filtre_min_completion_rate(dataset:pd.DataFrame, min_completion_rate: float):

    # Calculer le taux de valeurs manquantes dans chaque colonne
    missing_rates = dataset.isna().mean()
    print("heeeeloooo")
    # Filtrer les colonnes qui n'atteignent pas le taux minimal de complétion
    filtered_cols = missing_rates[missing_rates > min_completion_rate].index
    print(filtered_cols)
    
    return dataset.dropna(filtered_cols, inplace=True)


import mlflow
from mlflow.tracking import MlflowClient


def yield_artifacts(run_id, path=None):
    """Yield all artifacts in the specified run"""
    client = MlflowClient()
    for item in client.list_artifacts(run_id, path):
        if item.is_dir:
            yield from yield_artifacts(run_id, item.path)
        else:
            yield item.path


def fetch_logged_data(run_id):
    """Fetch params, metrics, tags, and artifacts in the specified run"""
    client = MlflowClient()
    data = client.get_run(run_id).data
    # Exclude system tags: https://www.mlflow.org/docs/latest/tracking.html#system-tags
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = list(yield_artifacts(run_id))
    return {
        "params": data.params,
        "metrics": data.metrics,
        "tags": tags,
        "artifacts": artifacts,
    }