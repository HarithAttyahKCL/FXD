import sys

#Static Variables that contain messages and allowed strings
USAGE_MESSAGE = "Usage: python src/main.py <ImageAddress> <method> <numberOfColours> <numberOfThreads>"
ALLOWED_METHODS = set(['naivemt','kmeansmt'])
METHODS_MESSAGE_ALLOWED = "For five args, <method> only accepts: " + str(ALLOWED_METHODS)
NUMBER_OF_COLOURS_MESSAGE_DIGIT = "<numberOfColours> must be a digit."
NUMBER_OF_COLOURS_MESSAGE_ZERO = "<numberOfColours> must be at least 1."
NUMBER_OF_THREADS_MESSAGE_DIGIT = "<numberOfThreads> must be a digit."
NUMBER_OF_THREADS_MESSAGE_ZERO = "<numberOfThreads> must be at least 1."

def validate_command():
    validate_length()
    validate_method()
    validate_numberOfColours()

def validate_length():
    if len(sys.argv) != 5:
        print(USAGE_MESSAGE)
        sys.exit(1)

def validate_method():
    if sys.argv[2] not in ALLOWED_METHODS:
       print(METHODS_MESSAGE_ALLOWED)
       sys.exit(1)

def validate_numberOfColours():
    if not sys.argv[3].isdigit():
        print(NUMBER_OF_COLOURS_MESSAGE_DIGIT)
        sys.exit(1)
    elif not int(sys.argv[3]) > 0:
        print(NUMBER_OF_COLOURS_MESSAGE_ZERO)
        sys.exit(1)

def validate_numberOfThreads():
    if not sys.argv[3].isdigit():
        print(NUMBER_OF_THREADS_MESSAGE_DIGIT)
        sys.exit(1)
    elif not int(sys.argv[3]) > 0:
        print(NUMBER_OF_THREADS_MESSAGE_ZERO)
        sys.exit(1)