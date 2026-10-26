"""
visualization.py
-----------------
Reusable plotting functions for EDA and cluster visualization.
All functions save the figure to results/figures/ AND display it inline
(when run inside a notebook), so the same function can be used for both
interactive exploration and generating report screenshots.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
FIGURES_DIR = "results/figures"


def _save(fig, filename):
    os.makedirs(FIGURES_DIR, exist_ok=True)
    path = os.path.join(FIGURES_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Saved figure -> {path}")


def plot_distribution(df, column, filename, bins=20, kde=True):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df[column], bins=bins, kde=kde, ax=ax, color="#4C72B0")
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_boxplot(df, column, filename, by=None):
    fig, ax = plt.subplots(figsize=(6, 4))
    if by:
        sns.boxplot(data=df, x=by, y=column, ax=ax)
        ax.set_title(f"{column} by {by}")
    else:
        sns.boxplot(y=df[column], ax=ax)
        ax.set_title(f"Boxplot of {column}")
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_correlation_heatmap(df, columns, filename):
    fig, ax = plt.subplots(figsize=(6, 5))
    corr = df[columns].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax, fmt=".2f")
    ax.set_title("Correlation Heatmap")
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_scatter(df, x, y, filename, hue=None, title=None):
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, palette="tab10", ax=ax, s=60, edgecolor="black")
    ax.set_title(title or f"{y} vs {x}")
    if hue:
        ax.legend(title=hue, bbox_to_anchor=(1.05, 1), loc="upper left")
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_elbow(k_values, wcss, filename):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(k_values, wcss, marker="o", color="#DD8452")
    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("WCSS (Inertia)")
    ax.set_title("Elbow Method for Optimal K")
    ax.set_xticks(list(k_values))
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_silhouette_scores(k_values, scores, filename):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(k_values, scores, marker="o", color="#55A868")
    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("Average Silhouette Score")
    ax.set_title("Silhouette Score vs K")
    ax.set_xticks(list(k_values))
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_clusters_2d(X, labels, x_label, y_label, filename, title, centers=None):
    """Scatter plot of two clustering features colored by cluster label."""
    fig, ax = plt.subplots(figsize=(7, 5))
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap="tab10", s=60, edgecolor="black")
    if centers is not None:
        ax.scatter(centers[:, 0], centers[:, 1], c="red", marker="X", s=250,
                   edgecolor="black", label="Centroids")
        ax.legend()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    legend1 = ax.legend(*scatter.legend_elements(), title="Cluster", bbox_to_anchor=(1.05, 1), loc="upper left")
    ax.add_artist(legend1)
    _save(fig, filename)
    plt.show()
    plt.close(fig)


def plot_pca_clusters(X_pca, labels, filename, title):
    fig, ax = plt.subplots(figsize=(7, 5))
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap="tab10", s=60, edgecolor="black")
    ax.set_xlabel("PCA Component 1")
    ax.set_ylabel("PCA Component 2")
    ax.set_title(title)
    legend1 = ax.legend(*scatter.legend_elements(), title="Cluster", bbox_to_anchor=(1.05, 1), loc="upper left")
    ax.add_artist(legend1)
    _save(fig, filename)
    plt.show()
    plt.close(fig)
