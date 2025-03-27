from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# Convert to DataFrame for easy visualization
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# 1. Visualize Original Features
sns.pairplot(df, hue='target', palette='Set2')
plt.suptitle("Pairplot of Original Iris Features", y=1.02)
plt.show()

# 2. Standardize the Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Visualize the distribution before and after scaling
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Before Scaling
axs[0].boxplot(X)
axs[0].set_title("Before Scaling")
axs[0].set_xticklabels(range(1, len(feature_names)+1))
axs[0].set_xticklabels(feature_names, rotation=45)

# After Scaling
axs[1].boxplot(X_scaled)
axs[1].set_title("after standardization")
axs[1].set_xticks(range(1, len(feature_names)+1))
axs[1].set_xticklabels(feature_names, rotation=45)

plt.tight_layout()
plt.show()

# 3. Apply PCA
pca = PCA(n_components=4)  # Keep all components for full variance
X_pca = pca.fit_transform(X_scaled)

# Explained variance plot
components = ["PC1", "PC2"]
plt.figure(figsize=(6, 4))
plt.bar(range(1, len(pca.explained_variance_ratio_)+1), pca.explained_variance_ratio_, tick_label=["PC1", "PC2", "PC3", "PC4"])
plt.ylabel('Explained Variance Ratio')
plt.title('PCA Explained Variance per Component')
plt.show()

# Visualize PCA-transformed data with actual labels
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=iris.target_names[y], palette='Set2')
plt.title("PCA Projection of Iris Dataset (True Labels)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title='Actual Class')
plt.show()

# 4. Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_pca)
labels = kmeans.labels_

# Visualize K-Means Clusters on PCA Data

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title("K-Means Clusters (PCA-Reduced Iris Data)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title='Cluster')
plt.show()
