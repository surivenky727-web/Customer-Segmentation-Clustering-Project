"""
evaluation.py
-------------
Clustering evaluation metrics.

IMPORTANT (see docs/project_report.md, section "Evaluation Methodology"):
This is an UNSUPERVISED learning project. There are no ground-truth labels
for "correct" customer segments, so classification metrics such as
accuracy, precision, recall, F1-score, or ROC-AUC DO NOT apply and are
intentionally NOT used anywhere in this project.

Instead we use internal clustering validation metrics, which judge cluster
quality using only the data and the resulting cluster assignments:

    - Silhouette Score        (range -1 to 1, higher is better)
    - Davies-Bouldin Index    (>= 0, lower is better)
    - Calinski-Harabasz Index (>= 0, higher is better)
    - WCSS / Inertia          (K-Means only, lower is better but always
                                decreases with more clusters - used only
                                for the Elbow Method, not as a final score)
"""

import numpy as np
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score,
)


def evaluate_clustering(X_scaled, labels, exclude_noise=False):
    """
    Compute Silhouette, Davies-Bouldin and Calinski-Harabasz scores.

    If `exclude_noise` is True (useful for DBSCAN), points labeled -1
    (noise) are excluded before computing the metrics, since noise points
    are not part of any cluster and would distort the scores.

    Returns a dict of metrics. If fewer than 2 clusters are present,
    metrics that require at least 2 clusters are returned as None.
    """
    X_eval = X_scaled
    labels_eval = np.asarray(labels)

    if exclude_noise:
        mask = labels_eval != -1
        X_eval = X_scaled[mask]
        labels_eval = labels_eval[mask]

    n_unique = len(set(labels_eval))

    metrics = {
        "n_clusters": n_unique,
        "silhouette_score": None,
        "davies_bouldin_index": None,
        "calinski_harabasz_index": None,
    }

    if n_unique >= 2:
        metrics["silhouette_score"] = round(float(silhouette_score(X_eval, labels_eval)), 4)
        metrics["davies_bouldin_index"] = round(float(davies_bouldin_score(X_eval, labels_eval)), 4)
        metrics["calinski_harabasz_index"] = round(float(calinski_harabasz_score(X_eval, labels_eval)), 4)

    return metrics


def cluster_profile(df, labels, features, cluster_col="Cluster"):
    """
    Build a per-cluster summary table (mean feature values + cluster size).
    This is the main tool for BUSINESS interpretation of clusters, i.e.
    turning cluster numbers (0, 1, 2, ...) into human-readable customer
    segment descriptions.
    """
    df = df.copy()
    df[cluster_col] = labels
    profile = df.groupby(cluster_col)[features].mean().round(2)
    profile["Count"] = df.groupby(cluster_col).size()
    profile["Percentage"] = (profile["Count"] / len(df) * 100).round(1)
    return profile.sort_index()
