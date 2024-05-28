import numpy as np
import cv2
import sys
import os

def save_images(foreground, background):
    # Create a directory named 'img' if it doesn't exist
    if not os.path.exists('img'):
        os.makedirs('img')

    # Save foreground and background images
    cv2.imwrite('img/foreground.jpg', foreground)
    cv2.imwrite('img/background.jpg', background)

def draw_mask(image):
    # Create a black mask of the same size as the image
    mask = np.zeros(image.shape[:2], np.uint8)

    # Initialize background and foreground models for GrabCut
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define rectangle for initial segmentation (you can change these values)
    rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)

    # Apply GrabCut algorithm
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Modify the mask to create a binary mask where 0 and 2 pixels are background and all others are foreground
    mask_binary = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    return mask_binary

def apply_grabcut(image, mask):
    # Create a new mask where background is black and foreground is white
    new_mask = np.zeros_like(image)
    new_mask[:, :, 0] = mask * 255
    new_mask[:, :, 1] = mask * 255
    new_mask[:, :, 2] = mask * 255

    # Multiply the original image with the mask to get foreground
    foreground = cv2.bitwise_and(image, new_mask)

    # Invert the mask
    inverted_mask = cv2.bitwise_not(mask)

    # Multiply the original image with the inverted mask to get background
    background = cv2.bitwise_and(image, cv2.merge([inverted_mask, inverted_mask, inverted_mask]))

    return foreground, background


# Load your image
image = cv2.imread(sys.argv[1])

# Draw a mask on the image
mask = draw_mask(image)

# Apply GrabCut algorithm
foreground, background = apply_grabcut(image, mask)

save_images(foreground=foreground,background= background)

