import methods.gmm as gmm
import methods.kmeans as kmeans
import methods.kmeansmt as kmeansmt
import methods.naive as naive
import methods.naivemt as naivemt

def apply_kmeans(image,numberOfColours) -> list:
    return kmeans.dominantColour_kmeans(image = image,numberOfColours= int(numberOfColours))

def apply_kmeansmt(image,numberOfColours,numberOfThreads) -> list:
    return kmeansmt.dominantColour_kmeansmt(image = image,numberOfColours= int(numberOfColours),num_threads= int(numberOfThreads))

def apply_naive(image,numberOfColours) -> list:
    return naive.dominantColour_naive(image = image,numberOfColours= int(numberOfColours))

def apply_naivemt(image,numberOfColours,numberOfThreads) -> list:
    return naivemt.dominantColour_naivemt(image = image,numberOfColours= int(numberOfColours),num_threads= int(numberOfThreads))

def apply_gmm(image,numberOfColours) -> list:
    return gmm.dominantColour_gmm(image = image,numberOfColours= int(numberOfColours))

ST_MAP = {
    "naive": apply_naive,
    "kmeans": apply_kmeans,
    "gmm": apply_gmm
}

MT_MAP = {
    "naivemt": apply_naivemt,
    "kmeansmt": apply_kmeansmt
}

def apply_method(image, parameters):
    if len(parameters) == 3:
        return ST_MAP[parameters[1]](image,parameters[2])
    if len(parameters) == 4:
        return MT_MAP[parameters[1]](image,parameters[2],parameters[3])