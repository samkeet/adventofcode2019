import os
import math

def getFuel(i):
    return int(math.floor(int(i)/3) - 2)

if __name__ == "__main__":
    with open("inputpart1.txt") as fp:
        sums = 0
        inputs = fp.readlines()
        for i in inputs:
            sums += getFuel(i)
        print sums