""" I say hello """
import sys

names = sys.argv[1:] if len(sys.argv) > 1 else ["world"]

print(f"Hello {' and '.join(names)}!")
