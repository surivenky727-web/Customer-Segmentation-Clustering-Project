# User & Technical Documentation

## 1. Overview

This project provides a Jupyter-notebook-based pipeline for segmenting
mall customers using K-Means and DBSCAN clustering. It is intended to be
run sequentially, notebook by notebook.

## 2. System Requirements

- Python 3.10 or later
- ~200 MB free disk space (dataset + generated figures/models)
- No GPU required

## 3. Installation

```bash
# 1. Clone or extract the project
cd customer-segmentation-ml

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook
```

## 4. Running the Project

Run the notebooks **in this order** (each depends on files saved by the
previous one):

1. `notebooks/01_data_understanding.ipynb` - loads and inspects the raw
   dataset.
2. `notebooks/02_preprocessing_and_eda.ipynb` - cleans, encodes, scales
   the data, saves `data/processed/mall_customers_processed.csv` and
   `data/processed/X_scaled.npy`, and performs EDA.
3. `notebooks/03_kmeans_clustering.ipynb` - selects K, trains K-Means,
   evaluates and visualizes clusters, tests new customers, saves
   `data/processed/kmeans_labels.npy` and
   `results/metrics/kmeans_model.pkl`.
4. `notebooks/04_dbscan_comparison.ipynb` - trains DBSCAN, compares
   against K-Means, analyzes noise points, tests new customers.

Use "Run All" in Jupyter for each notebook, top to bottom.

## 5. Project Structure

```
customer-segmentation-ml/
├── data/
│   ├── raw/                     Original dataset (Mall_Customers.csv)
│   └── processed/                Cleaned/scaled data + saved arrays
├── notebooks/                    4 sequential Jupyter notebooks
├── src/                          Shared, reusable Python modules
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── evaluation.py
│   └── visualization.py
├── results/
│   ├── figures/                  All generated plots (PNG)
│   ├── metrics/                  JSON metric files + saved model
│   └── tables/                   CSV result tables
├── docs/                         Full academic documentation (this folder)
├── presentation/                 Slide content for the academic presentation
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── PROJECT_COMPLETION_CHECKLIST.md
```

## 6. Using the `src/` Modules Directly (outside notebooks)

```python
from src.preprocessing import full_preprocessing_pipeline
from src.clustering import fit_kmeans
from src.evaluation import evaluate_clustering

raw_df, df, X, X_scaled, scaler = full_preprocessing_pipeline()
model, labels = fit_kmeans(X_scaled, n_clusters=5)
metrics = evaluate_clustering(X_scaled, labels)
print(metrics)
```

## 7. Assigning a New Customer to a Cluster (K-Means)

```python
import pickle
import pandas as pd
from src.preprocessing import CLUSTERING_FEATURES

with open('results/metrics/kmeans_model.pkl', 'rb') as f:
    saved = pickle.load(f)
model, scaler = saved['model'], saved['scaler']

new_customer = pd.DataFrame({
    'Age': [30], 'Annual Income (k$)': [60], 'Spending Score (1-100)': [70]
})
scaled = scaler.transform(new_customer[CLUSTERING_FEATURES])
cluster = model.predict(scaled)[0]
print(f"Assigned cluster: {cluster}")
```

## 8. Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: src` | Notebook run from wrong directory | Ensure notebooks are launched from the `notebooks/` folder, or `sys.path.append('..')` (already included in each notebook's first code cell) |
| Empty/garbled plots | Non-interactive backend | Restart the Jupyter kernel and re-run all cells |
| Different cluster numbers on rerun | Random seed not respected | Ensure `random_state=42` remains unchanged in `src/clustering.py` |

## 9. Regenerating All Results From Scratch

Delete the contents of `data/processed/` and `results/`, then re-run all
four notebooks in order. All figures, tables, and metrics will be
regenerated directly from `data/raw/Mall_Customers.csv`.
