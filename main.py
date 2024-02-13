import sys

from MondrianSolver import SolveMondrian
from Visualize import visualize

"""Python version >= 3.10 required"""
"""Numpy package required"""
def main():
    args = sys.argv
    if len(args) != 3:
        sys.stderr.write(f"Expected 2 arguments, got {len(args) - 1}")
        sys.exit(-1)

    try:
        dimension = int(args[1])
        max_depth = int(args[2])
    except ValueError as ve:
        sys.stderr.write(ve.__str__())
        sys.exit(-1)


    s = SolveMondrian(dimension, max_depth)
    visualize(s)


if __name__ == "__main__":
    main()