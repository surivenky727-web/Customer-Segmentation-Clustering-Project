# Project Proposal

## Title
**Customer Segmentation Using K-Means and DBSCAN Clustering**

## Problem Statement
Retail and mall businesses collect customer data (age, income, spending
behavior) but often lack a systematic way to translate this raw data into
actionable customer groups. Without segmentation, marketing campaigns,
loyalty programs, and customer engagement strategies are typically
one-size-fits-all, which is inefficient and reduces marketing ROI. This
project addresses the problem of automatically discovering meaningful,
data-driven customer segments using unsupervised Machine Learning.

## Application Domain
Retail Analytics / Customer Relationship Management (CRM) / Marketing
Analytics.

## Motivation
Understanding customer groups allows a business to:
- Design targeted marketing campaigns for specific segments.
- Identify high-value customers for loyalty/retention programs.
- Detect underperforming or unusual customer behavior for further review.
- Allocate marketing budget more efficiently.

As a CSE student, this project is also a practical entry point into
unsupervised Machine Learning, distance-based algorithms, and the
important distinction between supervised and unsupervised evaluation.

## Objectives
1. Collect and preprocess a suitable customer dataset.
2. Perform exploratory data analysis to understand customer
   characteristics.
3. Apply **K-Means clustering** as the primary segmentation algorithm,
   with the number of clusters chosen using the Elbow Method and
   Silhouette Analysis.
4. Apply **DBSCAN** as an enhancement/comparison algorithm to detect
   noise/outlier customers and clusters of arbitrary shape.
5. Evaluate both algorithms using appropriate unsupervised metrics
   (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index).
6. Interpret the resulting clusters in business terms.
7. Demonstrate assigning new/unseen customers to existing segments.
8. Produce complete academic documentation, a presentation, and a
   GitHub-ready repository.

## Proposed Methodology
Follow the standard unsupervised ML pipeline: data understanding, data
cleaning, encoding, feature selection, feature scaling, EDA, K-selection
(Elbow + Silhouette), K-Means training and evaluation, DBSCAN parameter
investigation and training, comparative analysis, and new-customer
demonstration. See `docs/project_report.md` (Methodology section) for
full detail, and `README.md` for the pipeline diagram.

## Dataset
**Mall Customer Segmentation Data** - 200 customer records with 5 columns
(`CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score
(1-100)`). Publicly available and widely used in customer segmentation
teaching material. See `docs/project_report.md` (Dataset Description) for
full details, including source and feasibility analysis.

## Algorithms
- **K-Means Clustering** (primary) - scikit-learn implementation.
- **DBSCAN** (enhancement/comparison) - scikit-learn implementation.
- **Agglomerative (Hierarchical) Clustering** (optional, brief reference
  comparison only).

## Expected Outcomes
- A working, reproducible clustering pipeline that segments mall customers
  into 4-6 interpretable groups.
- A clear comparison of K-Means vs. DBSCAN for this dataset, including
  identification of outlier/noise customers.
- Complete documentation, presentation material, and viva preparation
  suitable for a three-stage university review process.

## Feasibility
- **Data feasibility:** dataset is small, clean (no missing values or
  duplicates), and numeric-feature-rich - feasible to fully process within
  the project timeline.
- **Technical feasibility:** all algorithms used (K-Means, DBSCAN, PCA)
  are implemented in scikit-learn; no GPU or large-scale infrastructure
  required.
- **Academic feasibility:** scope is appropriately sized for a B.Tech
  corner-stone project - two mandatory algorithms, clear evaluation
  strategy, and a beginner-friendly explanation approach throughout.

## Project Milestones
See `docs/project_report.md` (Project Milestones section) and the table
below for the three-review timeline.

| Review | Focus | Target Deliverables |
|---|---|---|
| Review I | Planning | Proposal, literature survey, dataset selection, GitHub init |
| Review II | Development | Preprocessing, EDA, K-Means baseline & tuning, ~60-70% implementation |
| Review III | Finalization | DBSCAN, comparison, optimization, full documentation, GitHub-ready repo, viva prep |

## References
See `docs/literature_survey.md` for the full list of real, verified
references used in this project.
