# Dominant Colours:
Program that finds the dominant colours of an image and outputs a graph of the top N colours in 100x100 swatches.

## How to run:

- Navigate to project directory
- Create and activate virtual environment
```sh
python -m venv myenv
source venv/bin/activate  # On Windows use: .\myenv\Scripts\activate
```
- Install libs
```sh
pip install -r requirements.txt # Verify with 'pip list' if you wish.
```
## Execute this command 
```sh
python src/main.py <ImageAddress> <method> <numberOfColours>
```
- ImageAddress: the address of your image, ie:python main.py /home/harith/Downloads/trail-5yOnGsKUNGw-unsplash.jpg 
- nmethod: the method used for the selection of dominant colours. 'naive', 'kmeans' or 'gmm' currently
- numberOfColours: the number of dominant colours we want to return.

### Optional: Use Multithreaded commands:
```sh
python src/main.py <ImageAddress> <method> <numberOfColours> <numberOfThreads>
```
- ImageAddress: the address of your image, ie:python main.py /home/harith/Downloads/trail-5yOnGsKUNGw-unsplash.jpg 
- nmethod: the method used for the selection of dominant colours. Either 'naivemt' or 'kmeansmt'
- numberOfColours: the number of dominant colours we want to return.
- numberOfThreads: the number of threads the program will use.


