import sys
import cv2
import time
from methods import method
import validators.validate as validator
import colour_swatches 

# Run any validations on command.
validator.validate_command()

# Store start time
start_time = time.time() 

# Define list of parameters for use by method:
'''
    index 0: image path
    index 1: method name
    index 2: number of colours
    index 3: number of Threads
'''
params = []

# Extract variables from command-line arguments
for argument in range(1,len(sys.argv)):
    params.append(sys.argv[argument])

# Read the image
image = cv2.imread(params[0])

# Check if the image was successfully loaded
if image is not None:
    print("Image loaded successfully.")
else:
    print("Failed to load the image.")
    sys.exit(1)

# find and print the N dominant colours using method
dominants = method.apply_method(image, params)
stop_time = time.time() - start_time
print("Time Elapsed: " + str(stop_time) + " seconds")
print(str(dominants))
colour_swatches.display_colours(dominants)