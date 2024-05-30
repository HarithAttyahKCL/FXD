import sys
import validators.fiveargs as fiveargs
import validators.fourargs as fourargs

def validate_command():
    if len(sys.argv) == 4:
        fourargs.validate_command()
        return
    if len(sys.argv) == 5:
        fiveargs.validate_command()
        return
    print("Commands of Length 4 or 5 only")
    exit(1)
