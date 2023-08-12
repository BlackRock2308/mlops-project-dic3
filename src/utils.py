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
