import sys

def validate_command():
    validate_length()
    validate_method()
    validate_numberOfColours()

def validate_length():
    if len(sys.argv) != 4:
        print("Usage: python src/main.py <ImageAddress> <naive/kmeans> <numberOfColours>")
        sys.exit(1)

def validate_method():
    if sys.argv[2] != 'naive' and sys.argv[2] != 'kmeans':
       print("<naive/kmeans> only accepts 'naive' or 'kmeans'")
       sys.exit(1)

def validate_numberOfColours():
    if not sys.argv[3].isdigit():
        print("<numberOfColours> must be a digit")
        sys.exit(1)