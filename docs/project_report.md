# Project Report

## Customer Segmentation Using K-Means and DBSCAN Clustering

---

## 1. Abstract

This project implements an unsupervised Machine Learning system for
customer segmentation using the **Mall Customer Segmentation Data**
(200 customers, 5 features). **K-Means clustering** is used as the
primary segmentation algorithm, with the number of clusters selected
using the Elbow Method and Silhouette Analysis (final K = 5). **DBSCAN**
is applied as an enhancement/comparison algorithm to detect noise/outlier
customers and clusters of arbitrary density-based shape. Both algorithms
are evaluated using internal clustering metrics (Silhouette Score,
Davies-Bouldin Index, Calinski-Harabasz Index) rather than classification
metrics, since no ground-truth customer labels exist. The resulting
segments are interpreted in business terms (e.g. high income/high
spending, low income/low spending), and the pipeline is demonstrated on
new/unseen customer records. K-Means achieved a Silhouette Score of
0.4166; DBSCAN (eps=0.5, min_samples=6) achieved 0.5278 on
non-noise points while flagging 33% of customers as noise/outliers for
manual review.

## 2. Introduction

Businesses that interact with large numbers of customers - such as retail
stores and shopping malls - benefit from understanding their customer
base as distinct groups rather than as one undifferentiated population.
Clustering, an unsupervised Machine Learning technique, allows such
groups to be discovered automatically from data, without requiring
pre-labeled examples of "correct" segments.

## 3. Problem Statement

Given a dataset of customer demographic and behavioral attributes (age,
income, spending score), automatically identify meaningful, distinct
customer segments that can support targeted marketing and business
decision-making, without relying on manually pre-defined rules or
labels.

## 4. Motivation

Manual or rule-based segmentation (e.g. "age > 40 = senior segment") is
rigid and often misses non-obvious patterns in customer behavior.
Data-driven clustering can reveal segments that are not obvious from a
single feature alone (e.g. customers with high income but low spending -
a segment that would be missed by an income-only rule).

## 5. Objectives

See `docs/project_proposal.md` (Objectives section) for the full list.
In summary: preprocess data, explore it, apply K-Means (primary) and
DBSCAN (enhancement), evaluate with appropriate unsupervised metrics,
interpret clusters in business terms, and demonstrate new-customer
assignment.

## 6. Application Domain

Retail Analytics / Customer Relationship Management (CRM) / Marketing
Analytics.

## 7. Literature Survey

See `docs/literature_survey.md` for the complete survey, covering the
foundational DBSCAN paper (Ester et al., 1996), its generalization
(Sander et al., 1998), and several applied K-Means customer segmentation
papers, along with the specific gaps this project addresses.

## 8. Existing System

Traditional customer segmentation in many small/medium retail businesses
relies on manually defined rules or simple demographic bucketing (e.g.
age brackets, gender, geography). These approaches:
- Do not adapt to actual purchasing/spending behavior.
- Cannot discover non-obvious combinations of features.
- Require manual updates as customer behavior changes.
- Provide no principled way to detect atypical/outlier customers.

## 9. Proposed System

An automated, data-driven clustering pipeline that:
1. Preprocesses raw customer data (cleaning, scaling).
2. Applies K-Means to produce a stable, complete segmentation of every
   customer into one of K interpretable groups.
3. Applies DBSCAN as a complementary diagnostic layer to flag customers
   who do not fit cleanly into any dense group.
4. Provides a reusable, documented pipeline that can assign new customers
   to existing segments as new customer data arrives.

## 10. Requirement Analysis

**Functional requirements:**
- Load and clean customer data.
- Select and scale relevant numeric features.
- Determine an appropriate number of clusters for K-Means.
- Train and evaluate K-Means and DBSCAN models.
- Visualize and interpret clusters.
- Assign new/unseen customers to existing clusters.

**Non-functional requirements:**
- Reproducibility (fixed random seeds).
- Beginner-readability (Markdown explanations throughout notebooks).
- No fabricated results - all metrics/plots generated from the actual
  dataset.

**Technical requirements:** Python 3.10+, pandas, numpy, matplotlib,
seaborn, scikit-learn, Jupyter - all listed in `requirements.txt`.

## 11. Dataset Description

- **Name:** Mall Customer Segmentation Data
- **Source:** Publicly available dataset, originally distributed via
  Kaggle ("Mall Customer Segmentation Data") and widely mirrored in
  open-source ML teaching repositories. A local copy is included at
  `data/raw/Mall_Customers.csv` for reproducibility.
- **Records:** 200 customers
- **Features:** `CustomerID` (identifier, not used for clustering),
  `Gender` (categorical), `Age` (numeric), `Annual Income (k$)`
  (numeric), `Spending Score (1-100)` (numeric, assigned by the mall
  based on customer behavior)
- **Data quality:** 0 missing values, 0 duplicate rows (verified in
  `notebooks/01_data_understanding.ipynb`)
- **Feasibility:** small, clean, numerically rich dataset appropriate for
  an academic clustering project; see `docs/project_proposal.md` for the
  full feasibility discussion.

## 12. Methodology

1. **Preprocessing:** duplicate/missing-value check (none found),
   categorical encoding of Gender (for reference only), feature selection
   (Age, Annual Income, Spending Score), and `StandardScaler` feature
   scaling (required because K-Means/DBSCAN use Euclidean distance).
2. **Feature Selection:** Age, Annual Income, and Spending Score were
   selected as they jointly capture demographic and behavioral signal
   relevant to marketing decisions; `CustomerID` was excluded (identifier,
   not a feature) and Gender was excluded from the clustering feature set
   (see `src/preprocessing.py` for the reasoning).
3. **K-Means:** trained with `init='k-means++'`, `n_init=10`,
   `random_state=42`. K selected via Elbow Method (WCSS vs K plot) and
   Silhouette Analysis (K=2 to 10); final K=5.
4. **DBSCAN:** `eps` investigated via the k-distance graph and a grid
   search over `eps` in [0.3, 1.0] and `min_samples` in [4, 6]; final
   parameters chosen to balance number of clusters, noise ratio (5-40%),
   and Silhouette Score (excluding noise). Final: `eps=0.5`,
   `min_samples=6`.
5. **Evaluation:** Silhouette Score, Davies-Bouldin Index,
   Calinski-Harabasz Index for both algorithms (see Section 16).

## 13. Exploratory Data Analysis

Performed in `notebooks/02_preprocessing_and_eda.ipynb`: distribution
plots (Age, Income, Spending Score, Gender), boxplots/outlier checks,
correlation heatmap, and scatter plots (Income vs Spending Score, Age vs
Spending Score by Gender). Key findings: weak correlation between Age,
Income, and Spending Score (each carries distinct information); mild,
realistic income outliers; and clearly visible group structure in the
Income vs Spending Score scatter plot, motivating the clustering approach.

## 14. Model Development

K-Means and DBSCAN models were developed in
`notebooks/03_kmeans_clustering.ipynb` and
`notebooks/04_dbscan_comparison.ipynb` respectively, using the shared
`src/preprocessing.py`, `src/clustering.py`, and `src/evaluation.py`
modules to ensure consistent preprocessing and reproducible results
(fixed `random_state=42`).

## 15. Results

### K-Means (K=5)

| Cluster | Avg Age | Avg Income (k$) | Avg Spending Score | Count | % |
|---|---|---|---|---|---|
| 0 | 46.25 | 26.75 | 18.35 | 20 | 10.0% |
| 1 | 25.19 | 41.09 | 62.24 | 54 | 27.0% |
| 2 | 32.88 | 86.10 | 81.53 | 40 | 20.0% |
| 3 | 39.87 | 86.10 | 19.36 | 39 | 19.5% |
| 4 | 55.64 | 54.38 | 48.85 | 47 | 23.5% |

(Full table: `results/tables/kmeans_cluster_profile.csv`)

### DBSCAN (eps=0.5, min_samples=6)

- Clusters found: 5
- Noise/outlier points: 66 (33.0% of customers)
- See `results/tables/dbscan_parameter_grid.csv` for the full parameter
  grid search results.

## 16. Cluster Interpretation

| Cluster | Segment Label | Business Action |
|---|---|---|
| 0 | Older, low income, low spending | Low marketing priority |
| 1 | Young, moderate income, high spending | Growth segment - engagement offers |
| 2 | Middle-aged, high income, high spending | VIP / premium segment |
| 3 | Middle-aged, high income, low spending | Investigate barriers, personalized offers |
| 4 | Older, moderate income, moderate spending | Standard loyalty programs |

(Cluster numbers correspond to the table in Section 15; K-Means cluster
IDs are arbitrary integers with no inherent order.)

## 17. K-Means vs DBSCAN Comparison

| Metric | K-Means | DBSCAN |
|---|---|---|
| Number of clusters | 5 | 5 |
| Noise/outliers identified | 0 | 66 (33.0%) |
| Silhouette Score | 0.4166 | 0.5278 (excl. noise) |
| Davies-Bouldin Index | 0.8746 | 0.6043 (excl. noise) |
| Calinski-Harabasz Index | 125.10 | 144.38 (excl. noise) |
| Requires K in advance | Yes | No |
| Cluster shape assumption | Roughly spherical | Arbitrary (density-based) |
| Parameter sensitivity | Moderate | High |

**Discussion:** DBSCAN's higher Silhouette/Davies-Bouldin/Calinski-Harabasz
scores are computed only on the 67% of customers it considered "core"
cluster members, so they are not directly comparable to K-Means' scores
computed over all 200 customers - DBSCAN's numbers benefit from excluding
its hardest-to-cluster points. The real practical value of DBSCAN here is
not a higher score, but its ability to explicitly flag 66 customers whose
behavior does not fit any dense group - information K-Means cannot
provide, since it forces every customer into some cluster. See
`notebooks/04_dbscan_comparison.ipynb`, Section 9, for the full discussion
and business recommendation (use K-Means as the primary, stable
segmentation and DBSCAN as a periodic outlier-detection layer).

## 18. Error/Outlier Analysis

The 66 DBSCAN noise points were manually reviewed in
`notebooks/04_dbscan_comparison.ipynb`, Section 7. These represent
customers positioned in lower-density regions of the Age/Income/Spending
Score space - i.e., combinations of attributes that do not closely match
any of the five dense customer groups. This is not a data quality error;
it reflects genuine behavioral diversity in the dataset.

## 19. Limitations

- Dataset size (200 customers) is small; a production system should be
  validated on a larger, real transactional dataset.
- Only 3 numeric features were used for clustering; richer behavioral
  data (purchase frequency, recency, product categories) could produce
  more nuanced segments.
- DBSCAN's `eps`/`min_samples` were selected via a grid search over a
  reasonable but limited range; a different range could yield different
  "optimal" parameters.
- K-Means' spherical-cluster assumption may not perfectly match true
  customer group shapes.
- No true labels exist to verify segment correctness objectively; cluster
  quality is judged by internal metrics and business plausibility, not
  ground truth.

## 20. Future Enhancements

- Incorporate additional behavioral features (purchase frequency,
  recency, monetary value - an RFM-style feature set).
- Try K-Means initialization optimization methods referenced in the
  literature survey (e.g. PSO-based initialization).
- Deploy the pipeline as a small web service that scores new customers in
  real time.
- Periodically retrain the models as new customer data arrives, and track
  cluster stability over time.
- Experiment with Gaussian Mixture Models for soft (probabilistic)
  cluster membership.

## 21. Conclusion

This project successfully implements a complete, reproducible customer
segmentation pipeline using K-Means as the primary algorithm and DBSCAN
as an enhancement/comparison algorithm. Both algorithms were evaluated
using metrics appropriate for unsupervised learning, and the results were
interpreted in clear business terms. The pipeline was further validated
by demonstrating cluster assignment for new, unseen customer records.

## 22. References

See `docs/literature_survey.md` for the complete, verified reference
list.

---

## Appendix A: Why Standard Cross-Validation and Classification Metrics
Do Not Apply

This is an **unsupervised** learning project - there are no ground-truth
"correct" cluster labels to validate predictions against. Standard k-fold
cross-validation and classification metrics (accuracy, precision, recall,
F1, ROC-AUC) require known labels to measure prediction error, which does
not exist here. Instead:

- **Model/parameter selection** is performed using the Elbow Method
  (K-Means) and a parameter grid search evaluated with internal
  clustering metrics (DBSCAN) - this plays the analogous role that
  cross-validation plays in supervised learning: finding settings that
  generalize well to the structure of the data, using only the data
  itself (no external labels).
- **Model evaluation** uses Silhouette Score, Davies-Bouldin Index, and
  Calinski-Harabasz Index, which measure how compact and well-separated
  the discovered clusters are, directly from the data geometry.
- A fixed random seed (`random_state=42`) is used throughout to ensure
  the reported results are reproducible run-to-run, which substitutes for
  some of the "stability" guarantee that cross-validation provides in the
  supervised setting.

## Appendix B: Screenshot / Figure Index

All figures below were generated directly from the dataset (no fabricated
or placeholder images) and are saved under `results/figures/`:

| File | Description |
|---|---|
| `eda_age_distribution.png` | Age distribution histogram |
| `eda_income_distribution.png` | Annual income distribution histogram |
| `eda_spending_distribution.png` | Spending score distribution histogram |
| `eda_gender_count.png` | Gender count plot |
| `eda_boxplot_age.png` / `_income.png` / `_spending.png` | Outlier boxplots |
| `eda_correlation_heatmap.png` | Feature correlation heatmap |
| `eda_income_vs_spending.png` | Income vs Spending Score scatter |
| `eda_age_vs_spending_gender.png` | Age vs Spending Score by Gender |
| `kmeans_elbow_plot.png` | Elbow Method (WCSS vs K) |
| `kmeans_silhouette_scores.png` | Silhouette Score vs K |
| `kmeans_clusters_income_spending.png` | K-Means clusters (2D) with centroids |
| `kmeans_clusters_pca.png` | K-Means clusters (PCA projection) |
| `dbscan_k_distance_graph.png` | k-distance graph for eps selection |
| `dbscan_clusters_income_spending.png` | DBSCAN clusters (2D), noise shown |
| `dbscan_clusters_pca.png` | DBSCAN clusters (PCA projection) |

If additional application-level screenshots are required by the
university (e.g. of the Jupyter interface itself running each notebook),
insert them here with the placeholder format:

`[SCREENSHOT PLACEHOLDER: <description>, insert from local Jupyter run]`
