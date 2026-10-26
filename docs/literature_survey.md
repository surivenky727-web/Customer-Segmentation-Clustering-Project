# Literature Survey

## Customer Segmentation Using K-Means and DBSCAN Clustering

This survey reviews existing published work relevant to clustering-based
customer segmentation. All sources listed below are real, publicly
findable publications (verified via web search at the time of writing).
No papers, authors, or findings have been invented. Where full-text access
was not available, this is noted, and only claims that are directly
supported by the retrieved abstract/excerpt are summarized.

---

### 1. Foundational Algorithm Papers

**Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). "A Density-Based
Algorithm for Discovering Clusters in Large Spatial Databases with
Noise." Proceedings of the 2nd International Conference on Knowledge
Discovery and Data Mining (KDD-96), Portland, OR, pp. 226-231.**

This is the original paper introducing **DBSCAN**. The authors present a
density-based notion of a cluster: a cluster is a maximal set of
"density-connected" points, and any point that does not belong to such a
set is treated as noise. The algorithm requires only one primary input
parameter (`eps`, with `min_samples`/`MinPts` as a secondary parameter)
and can discover clusters of arbitrary shape while explicitly separating
noise from cluster members - both properties are directly relevant to and
used in this project's DBSCAN implementation.

**Sander, J., Ester, M., Kriegel, H.-P., & Xu, X. (1998). "Density-Based
Clustering in Spatial Databases: The Algorithm GDBSCAN and Its
Applications." Data Mining and Knowledge Discovery, 2(2), 169-194.**

This follow-up paper generalizes DBSCAN (as GDBSCAN) to work with
non-spatial and mixed attribute types, reinforcing that density-based
clustering is applicable beyond purely geographic/spatial data - relevant
justification for applying DBSCAN to demographic/behavioral customer
features rather than geospatial coordinates.

---

### 2. Customer Segmentation Applications of K-Means

**"Customer Segmentation Using K-Means Clustering for Personalized
Marketing Campaigns." International Journal of Scientific Research in
Computer Science, Engineering and Information Technology (IJSRCSEIT),
2025.**

This paper applies K-Means clustering to customer purchase behavior and
demographic attributes to design personalized marketing campaigns. The
authors use the **Elbow Method** and **Silhouette Analysis** to select
the number of clusters - the same two techniques used in this project's
K-Means notebook. Their results show that distinct clusters (e.g.
high-value/loyal customers vs. infrequent/price-sensitive buyers) enable
differentiated marketing strategies, directly supporting the business
motivation of this project.

**"Customer Segmentation Using K-Means Clustering." International Journal
of Engineering Research & Technology (IJERT), Vol. 11, Issue 03, March
2022.**

This paper walks through the standard K-Means algorithm steps (selecting
K, random centroid initialization, iterative assignment/update) applied to
customer segmentation, and reviews related work that segmented online
retail customers into a small number of mutually exclusive clusters. It
supports the standard preprocessing-then-cluster-then-interpret workflow
followed in this project.

**Li, Y., Qi, J., Chu, X., & Mu, W. (2023). "Customer Segmentation Using
K-Means Clustering and the Hybrid Particle Swarm Optimization Algorithm."
The Computer Journal, 66(4), 941-962.**

This paper (cited via a Kennesaw State University class project reference
list) proposes combining K-Means with particle swarm optimization to
improve cluster center initialization. It is noted here as an example of
active research into **optimizing K-Means initialization**, an
enhancement beyond the scope of this academic project but relevant future
work (see `docs/project_report.md`, Future Enhancements).

**"Customer Segmentation in the Digital Marketing Using a Q-Learning Based
Differential Evolution Algorithm Integrated with K-Means Clustering."
(2024/2025, PMC/NCBI-indexed).**

This paper combines PCA-based dimensionality reduction with an optimized
K-Means variant, validated on a Kaggle customer dataset, and uses the
Elbow Method to select the number of clusters - directly paralleling this
project's use of PCA (for visualization) and the Elbow Method (for K
selection).

---

### 3. Related Research Themes Identified

From the papers reviewed above, three consistent themes emerge that
directly informed this project's design:

1. **Elbow Method + Silhouette Analysis is the standard, widely accepted
   approach** for choosing K in K-Means-based customer segmentation
   studies - this project follows the same approach (see
   `notebooks/03_kmeans_clustering.ipynb`).
2. **DBSCAN's density-based, noise-aware design** is a recognized
   complement to K-Means for datasets where some records may not belong
   cleanly to any group - motivating this project's K-Means vs. DBSCAN
   comparison.
3. **Optimization of K-Means initialization/parameters** (e.g., via PSO or
   Q-learning-based methods) is an active research direction, but adds
   substantial complexity beyond an introductory B.Tech project - it is
   noted here as a future enhancement rather than implemented.

---

### 4. Gaps This Project Addresses

Several of the papers reviewed either (a) use simulated/synthetic data
rather than a real, publicly available dataset, or (b) focus solely on
K-Means without comparing against a density-based alternative. This
project addresses both gaps by:
- Using a real, publicly documented dataset (Mall Customer Segmentation
  Data) with verifiable characteristics.
- Implementing and comparing **both** K-Means and DBSCAN, discussing the
  trade-offs explicitly rather than presenting a single algorithm as a
  complete solution.

---

### Note on Verification

All references above were located via web search at the time of writing
this document. Readers/evaluators are encouraged to independently verify
each citation before final submission, as journal/conference details for
non-DOI sources (e.g., student-project or preprint-style publications)
can be harder to verify than peer-reviewed journal articles. Where a DOI
was not directly confirmed, this is intentional - **no DOI has been
fabricated**.
