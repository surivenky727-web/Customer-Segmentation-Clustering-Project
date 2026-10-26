# How This Project Works & ML Concepts Used

*(A plain-language summary to study alongside `docs/viva_preparation.md`.)*

## How This Project Works, Step by Step

1. **We start with raw customer data** - a table of 200 customers with
   age, gender, income, and a spending score.
2. **We clean it** - check for missing values and duplicates (there were
   none, but we check anyway).
3. **We select the features that matter for grouping customers**: Age,
   Annual Income, and Spending Score.
4. **We scale those features** so that a big number (income, up to 137)
   doesn't unfairly dominate a smaller-range number (spending score,
   1-100) when the algorithm measures "distance" between customers.
5. **We explore the data visually** to understand it before modeling -
   this is exactly like an engineer reading requirements before writing
   code.
6. **We let K-Means find groups automatically.** We first figure out
   *how many* groups make sense (K=5, using the Elbow Method and
   Silhouette Score), then let the algorithm sort every customer into
   one of those 5 groups based on how similar they are to each other.
7. **We let DBSCAN find groups differently.** Instead of forcing every
   customer into a group, DBSCAN only forms a group where customers are
   packed closely together, and it's allowed to say "this customer
   doesn't really fit anywhere" (noise).
8. **We measure how good the groups are** using metrics designed for
   this situation (no right/wrong answer to check against, so we measure
   how tight and separated the groups are instead).
9. **We translate the groups into English** - not just "Cluster 2," but
   "high income, high spending -> VIP customers."
10. **We test the whole pipeline on brand-new, made-up customers** to
    prove it would work in a real, ongoing system.

## ML Concepts Used (Quick Glossary)

- **Unsupervised Learning** - learning patterns from data that has no
  "correct answer" labels.
- **Clustering** - grouping similar data points together.
- **Feature** - a measurable property of the data (e.g. Age, Income).
- **Feature Scaling** - putting features on the same numeric range so
  distance-based algorithms treat them fairly.
- **Euclidean Distance** - the "straight-line" distance between two
  points, used by K-Means and DBSCAN to decide how similar two customers
  are.
- **Centroid** - the average point (center) of a cluster.
- **K-Means** - clustering algorithm that assigns every point to the
  nearest of K centroids, then updates the centroids, repeatedly.
- **Elbow Method** - a graph-based technique to pick a good value of K.
- **Silhouette Score** - a number showing how well-separated clusters are.
- **DBSCAN** - clustering algorithm that groups dense regions of points
  and labels sparse points as noise, without needing K specified upfront.
- **eps / min_samples** - DBSCAN's two parameters controlling how
  "close" and "how many" points must be to count as a dense region.
- **Noise Point** - a point DBSCAN could not fit into any dense cluster.
- **PCA (Principal Component Analysis)** - a way to compress many
  features into 2 for plotting, used here *only* for visualization.
- **Davies-Bouldin Index / Calinski-Harabasz Index** - additional
  unsupervised metrics used alongside Silhouette Score for a fuller
  picture of cluster quality.
- **Random Seed / random_state** - a fixed starting point for randomness
  so results are reproducible every time the code runs.

## Study Priority Before Viva

If short on time, study (in this order):
1. `docs/viva_preparation.md` (all 23 Q&A)
2. This file
3. `notebooks/03_kmeans_clustering.ipynb` Markdown cells
4. `notebooks/04_dbscan_comparison.ipynb` Markdown cells
5. `docs/project_report.md` Sections 15-18 (Results, Interpretation, Comparison)
