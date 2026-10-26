# Presentation Content
## Customer Segmentation Using K-Means and DBSCAN Clustering

*(12-15 slides. Convert each `##` section below into one slide. Speaker
notes are included under each slide as italics.)*

---

## Slide 1: Title
**Customer Segmentation Using K-Means and DBSCAN Clustering**
B.Tech CSE Machine Learning Corner-Stone Project
[Student Name] | [University Name] | [Date]

*Speaker notes: Introduce yourself and the project topic in one sentence.*

---

## Slide 2: Problem Statement
Retail businesses collect customer data but lack a systematic way to
turn it into actionable groups. This project builds an automated,
data-driven segmentation pipeline using unsupervised Machine Learning.

*Speaker notes: Emphasize "no manual rules, no pre-labeled data."*

---

## Slide 3: Motivation
- Manual/rule-based segmentation is rigid and misses non-obvious patterns
- Data-driven clustering reveals hidden customer groups
- Enables targeted marketing, loyalty programs, better ROI

*Speaker notes: Give one concrete example - e.g. "high income but low
spending" customers who a simple income-only rule would miss.*

---

## Slide 4: Objectives
1. Preprocess & explore customer data
2. Apply K-Means (primary algorithm)
3. Apply DBSCAN (enhancement/comparison)
4. Evaluate with unsupervised metrics
5. Interpret clusters & test on new customers

*Speaker notes: Keep to one line per objective, read them briskly.*

---

## Slide 5: Application Domain & Literature Survey
- Domain: Retail Analytics / CRM / Marketing Analytics
- DBSCAN: Ester et al. (1996), KDD-96
- Applied K-Means segmentation studies (IJERT 2022, IJSRCSEIT 2025)
- Gap addressed: real dataset + K-Means **and** DBSCAN comparison

*Speaker notes: Mention that full citations are in docs/literature_survey.md.*

---

## Slide 6: Dataset
- Mall Customer Segmentation Data: 200 customers, 5 columns
- CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)
- 0 missing values, 0 duplicates
- Publicly available, widely used for segmentation teaching

*Speaker notes: Show the dataset preview screenshot here (see results/figures or notebook 01).*

---

## Slide 7: Methodology / Pipeline
`Dataset -> Cleaning -> Encoding -> Feature Selection -> Scaling -> EDA ->
K-Selection -> K-Means -> Evaluation -> DBSCAN -> Comparison -> New
Customer Testing -> Conclusion`

*Speaker notes: Walk through the pipeline diagram left to right.*

---

## Slide 8: Data Preprocessing & EDA
- StandardScaler applied (required for distance-based clustering)
- Key EDA finding: clear visual grouping in Income vs Spending Score
- Weak correlation between Age/Income/Spending -> each feature useful

*Speaker notes: Show the Income vs Spending Score scatter plot here.*

---

## Slide 9: K-Means - Choosing K
- Elbow Method: WCSS vs K plot
- Silhouette Analysis: K=2 to 10
- Final K = 5 (supported by both methods)

*Speaker notes: Show the elbow plot and silhouette score plot side by side if possible.*

---

## Slide 10: K-Means Results
- 5 clusters, Silhouette Score 0.4166
- Segments range from "low income/low spending" to "high income/high spending"
- Centroid analysis used for business interpretation

*Speaker notes: Show the K-Means cluster scatter plot with centroids.*

---

## Slide 11: DBSCAN
- Density-based, no need to specify cluster count in advance
- Explicitly detects noise/outlier customers
- Parameters selected via k-distance graph + grid search (eps=0.5, min_samples=6)
- Result: 5 clusters, 33% of customers flagged as noise

*Speaker notes: Show the DBSCAN cluster plot with noise points highlighted.*

---

## Slide 12: K-Means vs DBSCAN
| | K-Means | DBSCAN |
|---|---|---|
| Clusters | 5 | 5 |
| Noise detected | 0 | 66 (33%) |
| Silhouette | 0.4166 | 0.5278 (excl. noise) |
| Needs K upfront | Yes | No |

*Speaker notes: Explain DBSCAN's higher score is computed on fewer (non-noise) points - not a direct "win."*

---

## Slide 13: Cluster Interpretation & Business Value
- Cluster 2 (high income, high spending): VIP segment -> premium offers
- Cluster 3 (high income, low spending): investigate & re-engage
- Cluster 0 (low income, low spending): low marketing priority

*Speaker notes: Pick 2-3 clusters and explain the recommended business action for each.*

---

## Slide 14: Conclusion & Future Scope
- Built a complete, reproducible segmentation pipeline
- K-Means: stable, complete segmentation; DBSCAN: outlier detection
- Future: RFM features, optimized initialization, GMM soft clustering

*Speaker notes: End on the practical takeaway - both algorithms together give a fuller picture than either alone.*

---

## Slide 15: Demo / GitHub / Thank You
- Live demo: new customer -> assigned cluster (notebooks 03 & 04)
- Full code & docs: [GitHub repository link]
- Thank you - Questions?

*Speaker notes: Have notebook 03's "new customer" cell ready to run live if time allows.*
