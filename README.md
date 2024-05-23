# Technical Challenge for FXDigital
This README documents my thoughts and attempt at the technical.

## Challenge 1: Find the most dominant colour of an image. (Most Frequent)
- The program accepts a image file as an input, this can be any common file
- The image is loaded and its pixels are read. The colours are compared. The problem may be simplified by reducing the colour space (ie rounding RGB values)
- the program must output <ins>RGB Values</ins> of the dominant colour.

### Initial thoughts on Challenge 1:
This problem can be approached using a naive solution: 
- create a dictionary using RGB codes as keys and count as values. 
- Iterate through the list of pixels the image
- Detect the RGB of a pixel and compare it to the dictionary. If a key is found then the value must update, if not: add the key and initialise value as 1. 
- This repeates until we have the final dictionary and we simply return the key with the highest value.

This approach has multiple problems, for an image with a large colour space the performance degrades and the count of a specific value might be meaningless in the case that an image has a large range of RGB values. Wouldnt it be better to have some kind of statistical
calculation using the dominant colours instead?

 **Note:** Another idea I have is another optimisation, consider using a lossless compression algorithm and then performing the algorithm as this reduces the amount of data required to process without losing colour accuracy.

### This is actually a clustering problem!
Returning back to the original intuition of using a more sensible measure of dominance than a simple pixel count, performing a clustering algorithm like kmeans can produce for us clusters of dominant colours and then we can simple retrieve the mean of the most dominant (ie the biggest) cluster. Adopting this approach not only improves our solution for Challenge 1, we actually spoil ourselves of some of the fun awaiting us in Challenge 2, because ranking our clusters in terms of size also produces us a ranking of the dominant colours!

 **Note:** Although this approach is promising we have to manually set up k (the amount of clusters). The number of clusters will affect the results produced by the algorithm, might be worth investigating both naive and kmeans with multiple ks. 

PS: worry about Docker and scalability later, try and focus on visualising results?
