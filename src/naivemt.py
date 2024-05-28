import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import threading

# Create a lock to ensure thread-safe access to the shared dictionary
lock = threading.Lock()

def find_dominant_colours(image: np.ndarray, result_dict: dict):
    """
    Finds the dominant colours in an image using a naive approach of finding modal rgb colours. 
    Args:
        image: ndarray representing a cv2 image
        result_dict: A shared dictionary for storing the result counts
    """
    # Convert BGR to RGB and flatten:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flat = rgb_image.reshape(-1, 3)

    # Using our dictionary/hashmap to store counts
    for rgb in flat:
        rgb_tuple = tuple(rgb)
        with lock:  # Acquire the lock before accessing the shared dictionary
            result_dict[rgb_tuple] = result_dict.get(rgb_tuple, 0) + 1
        # Release the lock after updating the shared dictionary

def dominantColour_naivemt(image: np.ndarray, numberOfColours: int, num_threads: int) -> list:
    """
    Finds the dominant colours in an image using multiple threads.
    Args:
        image: ndarray representing a cv2 image
        numberOfColours: An integer representing the number of dominant colors to find.
        num_threads: An integer representing the desired number of threads.
    Returns:
        A list of RGB tuples representing the dominant colours.
    """
    # Create a shared dictionary for storing the result counts
    result_dict = {}

    # Split the image into chunks for multithreading
    height = image.shape[0]
    chunk_size = height // num_threads
    
    # Create a thread pool
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start_row = i * chunk_size
            end_row = start_row + chunk_size if i < num_threads - 1 else height
            thread_image = image[start_row:end_row, :, :]
            executor.submit(find_dominant_colours, thread_image, result_dict)
        
    # Sort the dictionary by value (count) and take the top numberOfColours items
    sorted_items = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)[:numberOfColours]    

    # Extract the RGB tuples from the sorted items
    colourList = [rgb_value for rgb_value, _ in sorted_items]

    return colourList
