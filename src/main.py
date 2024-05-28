import sys
import cv2
import time
import naive, kmeans, naivemt, kmeansmt
import validate
import colour_swatches 

NUMBER_OF_THREADS = 2

# Define Methods and method handling
def handle_naive(image, numberOfColours):
    dominants = naive.dominantColour_naive(image = image,numberOfColours= int(numberOfColours))
    stop_time = time.time() - start_time
    print("Time Elapsed: " + str(stop_time) + " seconds")
    colour_swatches.display_colours(dominants)

def handle_kmeans(image, numberOfColours):
    dominants = kmeans.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours))
    stop_time = time.time() - start_time
    print("Time Elapsed: " + str(stop_time) + " seconds")
    colour_swatches.display_colours(dominants)

def handle_naivemt(image, numberOfColours):
    dominants = naivemt.dominantColour_naivemt(image = image,numberOfColours= int(numberOfColours),num_threads= NUMBER_OF_THREADS)
    stop_time = time.time() - start_time
    print("Time Elapsed: " + str(stop_time) + " seconds")
    colour_swatches.display_colours(dominants)

def handle_kmeansmt(image,numberOfColours):
    dominants = kmeansmt.dominantColour_kmeansmt(image = image,numberOfColours= int(numberOfColours),num_threads= NUMBER_OF_THREADS)
    stop_time = time.time() - start_time
    print("Time Elapsed: " + str(stop_time) + " seconds")
    colour_swatches.display_colours(dominants)

METHOD_MAP = {
    "naive": handle_naive,
    "kmeans": handle_kmeans,
    "naivemt": handle_naivemt,
    "kmeansmt": handle_kmeansmt
}

# Run any validations on command.
validate.validate_command()

# Store start time
start_time = time.time() 

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

# find and print the N dominant colours using method
METHOD_MAP[method](image, numberOfColours)