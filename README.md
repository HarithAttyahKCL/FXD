# Dominant Colours:
Program that finds the dominant colours of an image and outputs a graph of the top N colours in 100x100 swatches.

## How to run:

### Use Docker:
Navigate to the working directory and run the following commands:
```bash
 docker build -t fxdigitalapp .
```
```bash
 docker run -it fxdigitalapp
```

## Execute this command
```bash
python main.py <ImageAddress> <naive/kmeans> <numberOfColours>
```
- ImageAddress: the address of your image, ie:python main.py /home/harith/Downloads/trail-5yOnGsKUNGw-unsplash.jpg 
- naive/kmeans: the method used for the selection of dominant colours. Either 'naive' or 'kmeans'
- numberOfColours: the number of dominant colours we want to return.

