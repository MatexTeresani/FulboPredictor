from pathlib import Path

ROOT = Path(".")

folders = [
    "data/raw",
    "data/processed",
    "data/external",

    "models",
    "notebooks",

    "src",

    "src/config",
    "src/data",
    "src/features",
    "src/models",
    "src/api",
    "src/utils",

    "tests",
    "logs",
]

files = {
    "README.md": "# Match Predictor\n",

    ".gitignore": """
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/

models/*.pkl
models/*.joblib

logs/

.env

data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep
""",

    ".env": "",

    "src/__init__.py": "",
    "src/main.py": "",

    "src/config/__init__.py": "",
    "src/config/settings.py": "",

    "src/data/__init__.py": "",
    "src/data/downloader.py": "",
    "src/data/loader.py": "",
    "src/data/preprocessing.py": "",

    "src/features/__init__.py": "",
    "src/features/elo.py": "",
    "src/features/rolling_stats.py": "",
    "src/features/feature_builder.py": "",

    "src/models/__init__.py": "",
    "src/models/train.py": "",
    "src/models/predict.py": "",
    "src/models/evaluate.py": "",
    "src/models/tuning.py": "",

    "src/api/__init__.py": "",
    "src/api/main.py": "",

    "src/utils/__init__.py": "",
    "src/utils/logger.py": "",
    "src/utils/helpers.py": "",

    "tests/__init__.py": "",

    "data/raw/.gitkeep": "",
    "data/processed/.gitkeep": "",
    "data/external/.gitkeep": "",
}

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for filename, content in files.items():
    path = Path(filename)

    if not path.exists():
        path.write_text(content.strip() + "\n", encoding="utf-8")

print("Proyecto creado correctamente.")