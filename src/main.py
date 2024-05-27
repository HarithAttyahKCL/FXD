import sys
import cv2
import naive
import kmeans 
import validate
import colour_swatches 


# Run any validations on command.
validate.validate_command()

# Extract variables from command-line arguments
image_path = sys.argv[1]
method = sys.argv[2]
numberOfColours = sys.argv[3]

# Read the image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is not None:
    print("Image loaded successfully.")
else:
    print("Failed to load the image.")
    sys.exit(1)

# Using any specified method, find and print the N dominant colours.
if method == 'naive':
    dominants = naive.dominantColour_naive(image = image,numberOfColours= int(numberOfColours))
    colour_swatches.display_colours(dominants)

if method == 'kmeans':
    dominants = kmeans.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours))
    colour_swatches.display_colours(dominants)
