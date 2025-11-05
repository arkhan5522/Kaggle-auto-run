import os
from kaggle import KaggleApi
import time

NOTEBOOK = "abdulrehman0101/poster-automation/"  # <--- change if needed

print(f"🚀 Running Kaggle notebook remotely: {NOTEBOOK_REF}")

# Re-run the notebook directly on Kaggle servers
try:
    api.kernels_output(NOTEBOOK_REF)  # check if exists
    api.kernels_push_cli(NOTEBOOK_REF)  # older approach, but won't work for remote
except Exception as e:
    print(f"⚠️ Direct push failed: {e}")
    print("➡️ Using Kaggle API to re-run existing notebook...")
    api.kernels_pull(NOTEBOOK_REF, path='notebook')
    os.chdir('notebook')
    api.kernels_push('.')  # this uploads and re-runs the notebook
    print("🎉 Notebook execution triggered successfully!")
