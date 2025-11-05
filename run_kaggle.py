import os
import subprocess

# 🧠 Change this to your actual Kaggle username and notebook slug
NOTEBOOK_REF = "abdulrehman0101/poster-automation/"  # e.g., "arkhanai/poster-automation"
WORK_DIR = "notebook"

print(f"🚀 Running Kaggle notebook remotely: {NOTEBOOK_REF}")

# Create Kaggle API auth file from GitHub secrets
os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)
kaggle_path = os.path.expanduser("~/.kaggle/kaggle.json")

with open(kaggle_path, "w") as f:
    f.write(
        f'{{"username":"{os.getenv("KAGGLE_USERNAME")}","key":"{os.getenv("KAGGLE_KEY")}"}}'
    )

os.chmod(kaggle_path, 0o600)

# Pull the notebook (latest version)
subprocess.run(
    ["kaggle", "kernels", "pull", NOTEBOOK_REF, "-p", WORK_DIR, "-m"], check=True
)
print("✅ Notebook pulled successfully.")

# Push notebook (triggers re-run)
subprocess.run(["kaggle", "kernels", "push", "-p", WORK_DIR], check=True)
print("🎉 Notebook version pushed and run triggered successfully!")

# Optional: download output if notebook produces files
subprocess.run(["kaggle", "kernels", "output", NOTEBOOK_REF, "-p", "output"], check=False)
print("📦 Notebook output (if available) downloaded successfully.")
