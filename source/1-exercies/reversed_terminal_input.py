import sys
import random

# Usage: python reversed_terminal_input.py Hi
# iH

argv = sys.argv[1:]

reversed_array = reversed(argv)

revsered_sentense = " ".join(reversed_array)

print revsered_sentense
