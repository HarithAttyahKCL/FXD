# Dominant Colours:
Program that finds the dominant colours of an image and outputs a graph of the top N colours in 100x100 swatches.

## How to run:

- Navigate to project directory
- Create and activate virtual environment
```sh
virtualenv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```
- Install libs
```sh
pip install -r requirements.txt # Verify with 'pip list' if you wish.
```
## Execute this command
```sh
python main.py <ImageAddress> <method> <numberOfColours>
```
- ImageAddress: the address of your image, ie:python main.py /home/harith/Downloads/trail-5yOnGsKUNGw-unsplash.jpg 
- nmethod: the method used for the selection of dominant colours. Either 'naive' or 'kmeans' or the multithreaded versions.
- numberOfColours: the number of dominant colours we want to return.

