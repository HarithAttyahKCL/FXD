from . import *

NUMBER_OF_THREADS = 2

def kmeans(image,numberOfColours) -> list:
    return kmeans.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours))

def kmeansmt(image,numberOfColours) -> list:
    return kmeansmt.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours),num_threads= NUMBER_OF_THREADS)

def naive(image,numberOfColours) -> list:
    return naive.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours))

def naivemt(image,numberOfColours) -> list:
    return naivemt.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours),num_threads= NUMBER_OF_THREADS)

def gmm(image,numberOfColours) -> list:
    return gmm.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours))

METHOD_MAP = {
    "naive": naive,
    "kmeans": kmeans,
    "naivemt": naivemt,
    "kmeansmt": kmeansmt,
    "gmm": gmm
}