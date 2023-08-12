"""Settings"""
from pathlib import Path

# Home directory
HOME_DIR = Path.cwd().parent

# data
DATA_DIR = Path(HOME_DIR, "data")
DATA_DIR_INPUT = Path(DATA_DIR, "input")
DATA_DIR_OUTPUT = Path(DATA_DIR, "output")

# models
MODEL_DIR = Path(HOME_DIR, "models")
MODEL_NAME = "model_restaurant_revenue_prediction.dill"  # add on prefix the execution date (YYYYMMDD_{MODEL_NAME})

# reports: graphs, html, ...
REPORT_DIR = Path(HOME_DIR, "reports")

# Source de code
SRC_DIR = Path(HOME_DIR, "src")

# Notebook
NOTEBOOK_DIR = Path(HOME_DIR, "notebooks")

TIMEZONE = "UTC"

MODEL_PARAMS = {
    "MIN_COMPLETION_RATE": 0.5,  # min completion rate
    "FEATURES": [ 
                 ],
    "TARGET": "",
    "DATA_LEAKAGE_COLUMNS":[
        "",
    ]

}
