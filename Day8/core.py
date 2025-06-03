import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def df_summary(df):
    print("Shape of DataFrame:", df.shape)
    print("\n--- Data Types ---")
    print(df.dtypes)
    print("\n--- Missing Values ---")
    print(df.isnull().sum()[df.isnull().sum()>0])
    print("\n--- Summary Statistics ---")
    print(df.describe(include='all'))

def missing_report(df):
    return df.isnull().mean().sort_values(ascending= False)

def correlation_heatmap(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def outlier_summary(df):
    outliers = {}
    for col in df.select_dtypes(include=np.number).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        outliers[col] = ((df[col] < (q1 - 1.5 * iqr)) | (df[col] > (q3 + 1.5 * iqr))).sum()
    return pd.Series(outliers, name='outlier_count')

def plot_distributions(df):
    num_cols = df.select_dtypes(include=np.number).columns
    df[num_cols].hist(bins=30, figsize=(15, 8), color='skyblue')
    plt.tight_layout()
    plt.show()

def value_counts_all(df):
    return {col: df[col].value_counts() for col in df.select_dtypes(include='object')}