import os
from kaggle import KaggleApi
import time

NOTEBOOK = "abdulrehman0101/poster-automation/"  # <--- change if needed

def run_notebook():
    print(f"🚀 Running Kaggle notebook: {NOTEBOOK}")
    api = KaggleApi()
    api.authenticate()
    api.kernels_push(NOTEBOOK)
    print("✅ Notebook execution triggered successfully at", time.ctime())

if __name__ == "__main__":
    run_notebook()
