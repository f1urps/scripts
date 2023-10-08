#! /usr/bin/python3

# Program to print a hitomezashi pattern.


# Size of grid (in vertices, not characters)
SIDE_LENGTH = 30

# length of line segments connecting each vertex
SEGMENT_LENGTH = 1

###

import random

bitsX = [random.randrange(2) for i in range(SIDE_LENGTH)]
bitsY = [random.randrange(2) for i in range(SIDE_LENGTH)]

for y in range(SIDE_LENGTH):
    for i in range(SEGMENT_LENGTH):
        for x in range(SIDE_LENGTH):
            if x % 2 == bitsY[y] % 2 and i == SEGMENT_LENGTH - 1:
                print("_"*SEGMENT_LENGTH, end="")
            else:
                print(" "*SEGMENT_LENGTH, end="")

            if y % 2 == bitsX[x] % 2:
                print("|", end="")
            else:
                print(" ", end="")

        print("")








