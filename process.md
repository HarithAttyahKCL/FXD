# Technical Challenge for FXDigital
This documents my thoughts and attempt at the technical.

### Initial thoughts on the Challenge:
This problem can be approached using a naive solution: 
- create a dictionary using RGB codes as keys and count as values. 
- Iterate through the list of pixels the image
- Detect the RGB of a pixel and compare it to the dictionary. If a key is found then the value must update, if not: add the key and initialise value as 1. 
- This repeates until we have the final dictionary and we simply return the key with the highest value.

This approach works well if we want exact rgb values for an image, however for larger images, specifically ones with multiple shades of the same colour, if we want to instead look at dissimilar colours rather than focus on precise shades we need to use another metric like a mean instead.


### This is actually a clustering problem!
Returning back to the original intuition of using a more sensible measure of dominance than a simple pixel count, performing a clustering algorithm like kmeans can produce for us clusters of dominant colours and then we can simple retrieve the mean of the most dominant (ie the biggest) cluster.


### How to show the results?

As well as outputing the exact RGB values, I think it would be nice to see how the colours look compared to each other. So I decided to make a fashion inspired Swatch chart with the dominant colours.

## Further optimisations? Multithreading!

To my surprise, multithreading the naive solution seems to slow it down. This could be because multiple threads compete for the same resource/map in my implementation. I did also try giving each thread their own map, but this meant that joining all the maps in the end results in a greater wait time anyway due to the time complexity.