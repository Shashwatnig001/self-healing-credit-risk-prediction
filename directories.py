import os



folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "notebook",
    "src/ingestion",
    "src/validation",
    "src/preprocessing",
    "src/features",
    "src/training",
    "src/monitoring",
    "src/drift",
    "src/healing",
    "src/utils",
    "configs",
    "models",
    "logs",
    "reports",
    "dashboard",
    "api",
    "tests",
    "mlruns",
    "Dockerfile",
    "docker-compose.yml"  
]



for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Created folder: {folder}")



print("\n✅ Minimal project structure created successfully!")