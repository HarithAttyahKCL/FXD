import numpy as np
import matplotlib.pyplot as plt


def display_colours(colours: list):
    """
    Takes the list of RGB colours and produces swatches of colors from left to right in order of the list. list[0] == leftmost swatch.
    """
    swatch_size = 100
    swatches = np.zeros((swatch_size * len(colours), swatch_size, 3), dtype=np.uint8)
    
    for i, color in enumerate(colours):
        swatches[i * swatch_size:(i + 1) * swatch_size, :, :] = color

    plt.imshow(swatches.transpose(1,0,2))
    plt.axis('off')
    plt.show()