import cv2
import numpy as np
from sklearn.cluster import KMeans

def dominantColour_kmeans(image: np.ndarray, numberOfColours: int) -> list:
    """
    Finds the dominant colours in an image using K-means clustering.

    Args:
        image: ndarray representing a cv2 image
        numberOfColours: An integer representing the number of dominant colours to find.

    Returns:
        A list of RGB tuples representing the dominant colours.
    """

    # Convert BGR to RGB and flatten:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flat = rgb_image.reshape(-1, 3)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=numberOfColours)
    kmeans.fit(flat)

    # Get the cluster centers (colors)
    cluster_centers = kmeans.cluster_centers_.astype(int)

    # Get the counts of data points in each cluster
    _, counts = np.unique(kmeans.labels_, return_counts=True)

    # Sort the cluster centers based on the counts in descending order
    sorted_indices = np.argsort(counts)[::-1]
    sorted_cluster_centers = cluster_centers[sorted_indices]

    return sorted_cluster_centers.tolist()