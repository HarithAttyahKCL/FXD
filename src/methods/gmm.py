import cv2  
import numpy as np  
from sklearn.mixture import GaussianMixture  
  
def dominantColour_gmm(image: np.ndarray, numberOfColours: int) -> list:  
    """  
    Finds the dominant colours in an image using Gaussian Mixture Models (GMM).  
  
    Args:  
        image: ndarray representing a cv2 image  
        numberOfColours: An integer representing the number of dominant colours to find.  
  
    Returns:  
        A list of RGB tuples representing the dominant colours.  
    """  
  
    # Convert BGR to RGB and flatten:  
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    flat = rgb_image.reshape(-1, 3)  
  
    # Apply GMM clustering  
    gmm = GaussianMixture(n_components=numberOfColours)  
    gmm.fit(flat)  
  
    # Get the cluster means (colors)  
    cluster_means = gmm.means_.astype(int)  
  
    # Get the counts of data points in each cluster  
    _, counts = np.unique(gmm.predict(flat), return_counts=True)  
  
    # Sort the cluster means based on the counts in descending order  
    sorted_indices = np.argsort(counts)[::-1]  
    sorted_cluster_means = cluster_means[sorted_indices]  
  
    return sorted_cluster_means.tolist()  
