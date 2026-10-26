# Viva Preparation - Questions & Answers

Beginner-friendly answers for the project viva.

---

**Q1. What is Machine Learning?**
Machine Learning is a way of building software that learns patterns from
data instead of being explicitly programmed with fixed rules. The program
improves its behavior by analyzing examples rather than following
hand-written instructions for every case.

**Q2. What is unsupervised learning?**
Unsupervised learning is a type of Machine Learning where the data has no
labeled "correct answers." The algorithm finds structure or patterns in
the data on its own, instead of learning to predict a known label.

**Q3. Why is this project unsupervised?**
Because our customer dataset has no column saying "this customer belongs
to segment X." We don't know the true segments in advance - the whole
point of the project is to discover them from the data.

**Q4. What is clustering?**
Clustering is an unsupervised technique that groups data points so that
points in the same group (cluster) are more similar to each other than to
points in other groups.

**Q5. What is K-Means?**
K-Means is a clustering algorithm that partitions data into K groups. It
picks K initial cluster centers, assigns every point to its nearest
center, recalculates the centers as the average of their assigned points,
and repeats until the centers stop changing.

**Q6. Why did you choose K-Means?**
It is simple, fast, well-understood, and produces clear, complete
segmentation (every customer gets exactly one group), which is directly
useful for marketing decisions. It's also the standard, most-used
algorithm in customer segmentation literature.

**Q7. What is a centroid?**
A centroid is the "center point" of a cluster - the average position of
all data points currently assigned to that cluster. In K-Means, the
centroid is recalculated after every iteration.

**Q8. How did you select K (the number of clusters)?**
Using two methods together: the **Elbow Method** (plotting WCSS against K
and looking for the point where the improvement slows down) and
**Silhouette Analysis** (measuring how well-separated the clusters are
for each K). Both pointed to K=5.

**Q9. What is the Elbow Method?**
It's a technique for choosing K by plotting the Within-Cluster-Sum-of-
Squares (WCSS) for increasing values of K. WCSS always decreases as K
increases, but after a certain point the decrease becomes much smaller -
that "elbow" or bend in the curve is a good candidate for K.

**Q10. What is Silhouette Score?**
It's a number between -1 and 1 that measures how similar a point is to
its own cluster compared to the next-nearest cluster. Values closer to 1
mean well-separated, cohesive clusters; values near 0 mean overlapping
clusters; negative values mean points may be in the wrong cluster.

**Q11. Why is scaling important?**
K-Means and DBSCAN both measure distance between points. If one feature
(like income, which can be in the hundreds) has a much larger range than
another (like spending score, 1-100), it will dominate the distance
calculation and unfairly bias the clustering. Scaling (we used
StandardScaler) puts every feature on the same scale so each contributes
fairly.

**Q12. What is DBSCAN?**
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a
clustering algorithm that groups together points that are closely packed
(dense regions) and marks points in sparse/low-density regions as
"noise" instead of forcing them into a cluster.

**Q13. What is `eps` in DBSCAN?**
`eps` (epsilon) is the maximum distance between two points for them to be
considered neighbors. A smaller `eps` finds tighter, smaller clusters (and
more noise); a larger `eps` merges more points together.

**Q14. What is `min_samples` in DBSCAN?**
`min_samples` is the minimum number of neighboring points (within `eps`)
required for a point to be considered a "core point" that can start or
grow a cluster.

**Q15. Why compare K-Means with DBSCAN?**
To understand the trade-offs: K-Means gives every customer a segment but
assumes roughly round/spherical clusters; DBSCAN can find arbitrarily
shaped clusters and explicitly flags unusual customers as noise, which
K-Means cannot do. Comparing them gives a fuller picture than relying on
only one algorithm.

**Q16. What are outliers/noise points?**
They are data points that don't fit well into any dense group. In DBSCAN
these are explicitly labeled -1 ("noise"). In our project, about 33% of
customers were flagged this way - representing customers whose combined
age/income/spending pattern doesn't closely match any of the five main
groups.

**Q17. Why can't we use accuracy, precision, recall, or F1-score here?**
Those metrics require a known "correct" label to compare predictions
against (supervised learning). We have no ground-truth customer segment
labels - clustering is unsupervised, so we use different, appropriate
metrics: Silhouette Score, Davies-Bouldin Index, and Calinski-Harabasz
Index, which judge cluster quality directly from the data instead of
comparing to known answers.

**Q18. What are the limitations of this project?**
Small dataset (200 customers), only 3 numeric features used, DBSCAN
parameters chosen from a limited grid search, and no ground truth to
objectively confirm the segments are "correct" - cluster quality is
judged by internal metrics and business plausibility.

**Q19. How can the project be improved?**
Add more behavioral features (purchase frequency, recency, monetary
value), try optimized K-Means initialization methods from the literature,
retrain periodically as new data arrives, and try Gaussian Mixture Models
for probabilistic (soft) cluster membership.

**Q20. How would this work with new customers?**
For K-Means: the new customer's features are scaled using the *same*
fitted scaler used during training, then the model assigns them to the
nearest existing centroid using `.predict()`. For DBSCAN: since it has no
native `.predict()` method, we find the new customer's nearest neighbor in
the training data - if that neighbor is within `eps`, the new customer
gets that neighbor's cluster label; otherwise it is treated as noise.
Both approaches are demonstrated in notebooks 03 and 04.

**Q21. Why didn't you use cross-validation like in supervised learning?**
Standard k-fold cross-validation measures prediction error against known
labels on held-out folds - but we have no labels. Instead, we use the
Elbow Method and a parameter grid search (evaluated with internal
clustering metrics) to select K-Means' K and DBSCAN's `eps`/`min_samples`
- this serves a similar purpose (avoiding parameter choices that only
"look good" on the exact same run) while being appropriate for
unsupervised learning.

**Q22. What is PCA and why did you use it?**
PCA (Principal Component Analysis) reduces the number of dimensions in
data while preserving as much variation as possible. We used it only to
visualize our 3-feature (Age, Income, Spending Score) clustering result
in 2D, since humans can't easily see 3D scatter plots on paper/slides. It
was not used to change the actual features used for clustering.

**Q23. What does `random_state=42` do, and why does it matter?**
It fixes the random number generator's starting point, so operations that
involve randomness (like K-Means' initial centroid placement) produce the
exact same result every time the code is run. This makes the project's
results reproducible - a required property for academic work.
