"""
clustering.py
--------------
Wrapper functions around scikit-learn's KMeans, DBSCAN and Agglomerative
Clustering, plus helper functions for K-selection (Elbow Method) used
throughout the notebooks.

Centralizing this logic keeps notebooks readable (Markdown + short function
calls) instead of long blocks of raw scikit-learn code.
"""

import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

RANDOM_STATE = 42  # fixed seed for reproducibility


def compute_wcss(X_scaled, k_range=range(1, 11)):
    """
    Compute Within-Cluster-Sum-of-Squares (WCSS / inertia) for a range of K
    values. Used to draw the Elbow plot.
    """
    wcss = []
    for k in k_range:
        km = KMeans(n_clusters=k, init="k-means++", n_init=10, random_state=RANDOM_STATE)
        km.fit(X_scaled)
        wcss.append(km.inertia_)
    return list(k_range), wcss


def fit_kmeans(X_scaled, n_clusters: int):
    """Fit a K-Means model with the given number of clusters."""
    km = KMeans(
        n_clusters=n_clusters,
        init="k-means++",
        n_init=10,
        random_state=RANDOM_STATE,
    )
    labels = km.fit_predict(X_scaled)
    return km, labels


def fit_dbscan(X_scaled, eps: float, min_samples: int):
    """Fit a DBSCAN model with the given eps and min_samples."""
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(X_scaled)
    return db, labels


def fit_agglomerative(X_scaled, n_clusters: int):
    """Fit Agglomerative (hierarchical) clustering - optional comparison model."""
    agg = AgglomerativeClustering(n_clusters=n_clusters, linkage="ward")
    labels = agg.fit_predict(X_scaled)
    return agg, labels


def count_noise_points(labels: np.ndarray) -> int:
    """DBSCAN labels noise points as -1. Count them."""
    return int(np.sum(labels == -1))


def n_clusters_found(labels: np.ndarray) -> int:
    """Number of clusters found, excluding DBSCAN noise label (-1)."""
    unique_labels = set(labels)
    unique_labels.discard(-1)
    return len(unique_labels)
