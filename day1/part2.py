import os
import math

def getFuel(i):
    fuel = int(math.floor(i/3))
    if fuel == 0:
        return 0
    return fuel-2

def getModuleFuel(i):
    print(i)
    fuel_req = getFuel(i)
    total_fuel = 0
    while fuel_req > 0:
        total_fuel += fuel_req
        fuel_req = getFuel(fuel_req)
    return total_fuel

if __name__ == "__main__":
    with open("inputpart1.txt") as fp:
        total = 0
        inputs = fp.readlines()
        for i in inputs:
            total += getModuleFuel(int(i))
        # total = getModuleFuel(0)
        print total