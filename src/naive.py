import cv2
import numpy as np

def dominantColour_naive(image: np.ndarray, numberOfColours: int) -> list:
    """
    Finds the dominant colours in an image using a naive approach of finding modal rgb colours. 
    Args:
        image: ndarray representing a cv2 image
        numberOfColours: An integer representing the number of dominant colors to find.

    Returns:
        A list of RGB tuples representing the dominant colours.
    """

    # Convert BGR to RGB and flatten:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flat = rgb_image.reshape(-1,3)
    
    # Using our dictionary/hashmap to store counts
    rgb_counts = {}
    for rgb in flat:
        rgb_tuple=tuple(rgb)
        rgb_counts[rgb_tuple] = rgb_counts.get(rgb_tuple,0) + 1

    # Find the modal RGB values (modes) by sorting the dictionary by count
    modal_rgb_values = sorted(rgb_counts.items(), key=lambda x: x[1], reverse=True)[:numberOfColours]

    # Create a list and populate it with the colours.
    colourList = []
    for rgb_value, count in modal_rgb_values:
        colourList.append(rgb_value)

    return colourList