"""
preprocessing.py
-----------------
Data loading and preprocessing utilities for the Customer Segmentation project.

This module keeps every preprocessing step in ONE place so that the same
transformations can be reused consistently across:
    - the EDA notebook
    - the K-Means notebook
    - the DBSCAN notebook
    - the "new customer" prediction demo

Keeping preprocessing in a shared module (instead of copy-pasting code in
every notebook) avoids a very common beginner mistake: accidentally scaling
new/unseen data differently from the training data.
"""

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Columns used for clustering.
# Age, Annual Income and Spending Score are the three numeric, business
# meaningful features that describe WHO the customer is (age), WHAT they
# can spend (income) and HOW they actually behave (spending score).
CLUSTERING_FEATURES = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

# Get the project root directory (parent of the src folder)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "Mall_Customers.csv")
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "mall_customers_processed.csv")


def load_raw_data(path: str = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw Mall Customers dataset from disk."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic data cleaning.

    Steps performed:
        1. Drop exact duplicate rows (if any).
        2. Check / handle missing values (the raw dataset has none, but the
           check is still performed so the pipeline is safe to reuse on a
           different customer export that DOES contain missing values).
        3. Standardize column names (strip whitespace).

    Returns a cleaned copy of the dataframe.
    """
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before != after:
        print(f"Removed {before - after} duplicate rows.")

    # Handle missing values if present.
    # Numeric columns -> median imputation (robust to outliers).
    # Categorical columns -> mode imputation.
    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    if df[numeric_cols].isnull().sum().sum() > 0:
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].median())

    if df[categorical_cols].isnull().sum().sum() > 0:
        for col in categorical_cols:
            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].mode()[0])

    return df


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode the 'Gender' column numerically (Female=0, Male=1).

    NOTE: Gender is encoded and kept in the processed table for reference
    and for EDA (e.g. comparing spending patterns by gender), but it is
    NOT used as a clustering feature in the main pipeline. Mixing a binary
    categorical variable with continuous variables in a distance-based
    algorithm like K-Means/DBSCAN can distort the distance metric unless it
    is carefully weighted, which is beyond the scope of this project.
    """
    df = df.copy()
    if "Gender" in df.columns:
        df["Gender_Encoded"] = df["Gender"].map({"Female": 0, "Male": 1})
    return df


def select_features(df: pd.DataFrame, features=None) -> pd.DataFrame:
    """Select the numeric features used for clustering."""
    if features is None:
        features = CLUSTERING_FEATURES
    return df[features].copy()


def scale_features(X: pd.DataFrame, scaler: StandardScaler = None):
    """
    Scale features using StandardScaler (zero mean, unit variance).

    Scaling is essential for K-Means and DBSCAN because both algorithms
    rely on Euclidean distance. Without scaling, 'Annual Income' (which
    ranges up to ~137) would dominate the distance calculation over
    'Spending Score' (which ranges 1-100) and 'Age' (which ranges ~18-70).

    If a fitted `scaler` is supplied, it is reused (transform only) -
    this is important for consistently transforming NEW/unseen customer
    data using the statistics learned from the training data.
    """
    if scaler is None:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = scaler.transform(X)
    return X_scaled, scaler


def full_preprocessing_pipeline(path: str = RAW_DATA_PATH):
    """
    Convenience function that runs the full preprocessing pipeline and
    returns everything a notebook needs:
        raw_df, processed_df, X (unscaled features), X_scaled, scaler
    """
    raw_df = load_raw_data(path)
    df = clean_data(raw_df)
    df = encode_categorical(df)
    X = select_features(df)
    X_scaled, scaler = scale_features(X)
    return raw_df, df, X, X_scaled, scaler


if __name__ == "__main__":
    raw_df, df, X, X_scaled, scaler = full_preprocessing_pipeline()
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved to {PROCESSED_DATA_PATH}")
    print(df.head())
