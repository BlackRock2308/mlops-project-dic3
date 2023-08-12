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
    "FEATURES": ['Id', # Restaurant ID
                 'Open Date', # Opening date of a restaurant
                 'City', # City where the restaurant is located
                 'City Group', # Type of the city. Big cities, or Other.
                 'Type',  # Type of the restaurant. FC: Food Court, IL: Inline, DT: Drive-Thru, MB: Mobile
                 'P1', 
                 'P2', 
                 'P3', 
                 'P4',
                'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15',
                'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25',
                'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33', 'P34', 'P35',
                'P36', 
                'P37' 
       ],
    "TARGET": "revenue", """
    The revenue column indicates the transformed revenue
    of the restaurant in a given year and is the target of predictive analysis.
    """
    "DATA_LEAKAGE_COLUMNS":[
        "",
    ]

}
