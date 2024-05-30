import sys
import cv2
import time
from methods import method
import validate
import colour_swatches 

# Run any validations on command.
validate.validate_command()

# Store start time
start_time = time.time() 

# Extract variables from command-line arguments
image_path = sys.argv[1]
method_used = sys.argv[2]
numberOfColours = sys.argv[3]

# Read the image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is not None:
    print("Image loaded successfully.")
else:
    print("Failed to load the image.")
    sys.exit(1)

# find and print the N dominant colours using method
dominants = method.METHOD_MAP[method_used](image, numberOfColours)
stop_time = time.time() - start_time
print("Time Elapsed: " + str(stop_time) + " seconds")
print(str(dominants))
colour_swatches.display_colours(dominants)