# Customer Segmentation Using K-Means and DBSCAN Clustering

> B.Tech CSE Machine Learning Corner-Stone Project

## Overview

An unsupervised Machine Learning project that segments mall customers
into meaningful groups based on age, annual income, and spending
behavior. **K-Means** is used as the primary clustering algorithm; **DBSCAN**
is applied as an enhancement to detect outlier/noise customers and
compare against K-Means. The project follows a complete, reproducible
pipeline from raw data to business-interpretable customer segments.

## Problem Statement

Retail businesses collect customer data but often lack a systematic,
data-driven way to group customers for targeted marketing. This project
builds an automated clustering pipeline that discovers customer segments
directly from data, without manual rules or pre-labeled examples.

## Objectives

- Preprocess and explore a real customer dataset.
- Apply K-Means (with K chosen via Elbow Method + Silhouette Analysis).
- Apply DBSCAN to detect noise/outliers and compare against K-Means.
- Evaluate both algorithms using appropriate unsupervised metrics.
- Interpret clusters in business terms and test on new/unseen customers.

## Features

- Full EDA with 9+ purposeful visualizations.
- K-selection via Elbow Method and Silhouette Analysis.
- DBSCAN parameter tuning via k-distance graph + grid search.
- Cluster evaluation using Silhouette Score, Davies-Bouldin Index, and
  Calinski-Harabasz Index (no misapplied classification metrics).
- PCA-based 2D visualization of the full 3-feature clustering.
- New/unseen customer cluster-assignment demo for both algorithms.
- Fully reproducible (`random_state=42` throughout).

## Dataset

**Mall Customer Segmentation Data** - 200 records, 5 columns
(`CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score
(1-100)`). Publicly available; a local copy is included at
`data/raw/Mall_Customers.csv`. See `docs/project_report.md` for full
dataset details.

## Technologies / Libraries

Python 3, Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, Jupyter
Notebook. See `requirements.txt` for pinned versions.

## ML Algorithms

| Algorithm | Role |
|---|---|
| K-Means | Primary clustering algorithm |
| DBSCAN | Enhancement / comparison (outlier detection) |
| Agglomerative Clustering | Optional brief reference comparison |
| PCA | Dimensionality reduction for visualization only |

## Project Workflow

```
Dataset -> Data Understanding -> Cleaning -> Encoding -> Feature Selection
-> Scaling -> EDA -> Outlier Analysis -> K Selection -> K-Means
-> K-Means Evaluation -> Cluster Visualization -> Cluster Interpretation
-> DBSCAN -> DBSCAN Parameter Analysis -> DBSCAN Evaluation
-> K-Means vs DBSCAN Comparison -> New Customer Testing
-> Final Insights -> Conclusion
```

## Repository Structure

```
customer-segmentation-ml/
├── data/{raw,processed}/
├── notebooks/                 01_data_understanding, 02_preprocessing_and_eda,
│                               03_kmeans_clustering, 04_dbscan_comparison
├── src/                        preprocessing.py, clustering.py, evaluation.py, visualization.py
├── results/{figures,metrics,tables}/
├── docs/                        proposal, literature survey, report, user docs
├── presentation/                 slide content
├── requirements.txt, .gitignore, LICENSE
└── PROJECT_COMPLETION_CHECKLIST.md
```

## Installation

```bash
git clone <your-repo-url>
cd customer-segmentation-ml
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Running the Project

Run the four notebooks in `notebooks/` **in numeric order** (01 -> 04),
using "Run All" in Jupyter. See `docs/user_documentation.md` for full
instructions, troubleshooting, and code snippets for reusing the pipeline
outside notebooks.

## Results (Summary)

**K-Means (K=5):** Silhouette Score 0.4166, Davies-Bouldin 0.8746,
Calinski-Harabasz 125.10. Five interpretable segments identified, from
"low income / low spending" to "high income / high spending" (VIP).

**DBSCAN (eps=0.5, min_samples=6):** 5 density clusters, 66 customers
(33%) flagged as noise/outliers. Silhouette Score 0.5278 (on non-noise
points).

Full results, tables, and figures: `results/`. Full narrative results:
`docs/project_report.md` (Sections 15-18).

## Cluster Interpretation (K-Means)

| Cluster | Segment | Suggested Action |
|---|---|---|
| 0 | Older, low income, low spending | Low marketing priority |
| 1 | Young, moderate income, high spending | Growth segment - engagement offers |
| 2 | Middle-aged, high income, high spending | VIP / premium segment |
| 3 | Middle-aged, high income, low spending | Personalized offers |
| 4 | Older, moderate income, moderate spending | Standard loyalty programs |

## K-Means vs DBSCAN

DBSCAN's main practical advantage is not a "higher score" but its ability
to explicitly flag customers who don't fit any dense group - useful for
manual review. K-Means gives a stable, complete segmentation for every
customer and is simpler to maintain (one parameter vs. two). See
`docs/project_report.md` Section 17 for the full comparison table and
discussion.

## Limitations

Small dataset (200 records); only 3 numeric features used; DBSCAN
parameters selected from a bounded grid search; no ground-truth labels
exist to objectively verify segment "correctness." Full list:
`docs/project_report.md` Section 19.

## Future Enhancements

RFM-style feature expansion (recency, frequency, monetary value),
optimized K-Means initialization, periodic retraining, Gaussian Mixture
Models for soft clustering. Full list: `docs/project_report.md` Section 20.

## Authors / Team

- [Student Name] - B.Tech CSE, [University Name]

## Academic Project Disclaimer

This project was developed as an academic corner-stone project for a
B.Tech Computer Science and Engineering curriculum. It is intended for
learning and demonstration purposes.

## License

MIT License - see `LICENSE`.
