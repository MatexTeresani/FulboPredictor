match-predictor/
│
├── .venv/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_analysis.ipynb
│
├── src/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── data/
│   │   ├── downloader.py
│   │   ├── loader.py
│   │   └── preprocessing.py
│   │
│   ├── features/
│   │   ├── elo.py
│   │   ├── rolling_stats.py
│   │   └── feature_builder.py
│   │
│   ├── models/
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── evaluate.py
│   │   └── tuning.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   └── main.py
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── tests/
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore