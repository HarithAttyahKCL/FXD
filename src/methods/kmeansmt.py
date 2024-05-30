import cv2
import numpy as np
from sklearn.cluster import KMeans
from concurrent.futures import ThreadPoolExecutor

def dominantColour_kmeans_chunk(image_chunk: np.ndarray, numberOfColours: int) -> list:
    """
    Applies K-means clustering to a chunk of the image to find dominant colours.

    Args:
        image_chunk: ndarray representing a chunk of the cv2 image
        numberOfColours: An integer representing the number of dominant colours to find.

    Returns:
        The cluster centers (dominant colours) for the chunk.
    """
    flat = image_chunk.reshape(-1, 3)
    kmeans = KMeans(n_clusters=numberOfColours, n_init='auto')
    kmeans.fit(flat)
    return kmeans.cluster_centers_

def dominantColour_kmeansmt(image: np.ndarray, numberOfColours: int, num_threads: int) -> list:
    """
    Finds the dominant colours in an image using K-means clustering with multithreading.

    Args:
        image: ndarray representing a cv2 image
        numberOfColours: An integer representing the number of dominant colours to find.
        num_threads: An integer representing the desired number of threads.

    Returns:
        A list of RGB tuples representing the dominant colours.
    """
    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Split the image into chunks for multithreading
    height, width, _ = rgb_image.shape
    chunk_size = height // num_threads

    # Create a thread pool
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            start_row = i * chunk_size
            end_row = start_row + chunk_size if i < num_threads - 1 else height
            thread_image = rgb_image[start_row:end_row, :, :]
            futures.append(executor.submit(dominantColour_kmeans_chunk, thread_image, numberOfColours))
        
        # Collect results from all threads
        cluster_centers_list = []
        for future in futures:
            cluster_centers_list.extend(future.result())

    # Combine cluster centers from all chunks
    all_flat = np.vstack(cluster_centers_list)
    kmeans = KMeans(n_clusters=numberOfColours, n_init='auto')
    kmeans.fit(all_flat)

    # Get the final cluster centers (dominant colours)
    final_cluster_centers = kmeans.cluster_centers_.astype(int)

    return final_cluster_centers.tolist()

