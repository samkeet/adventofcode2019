from pprint import pprint
import os

def getUniquePlanets(orbits):
    planets = set()
    for orbit in orbits:
        center, orbiter = orbit.split(")")
        planets.add(center)
        planets.add(orbiter)

    return list(planets)

def generateGraph(orbits):
    orbit_map = {}
    for orbit in orbits:
        center, orbiter = orbit.split(")")
        orbit_map[orbiter] = center

    return orbit_map
        
def getPathCount(planets, orbits):
    print(orbits)
    count = 0
    for planet in planets:
        while planet in orbits:
            count += 1
            planet = orbits[planet]

    return count

'''Approach 1:
Generate a map of 
Orbitter -> List of Planets being Orbitted direcly or indirectly

But this one assumed that the input list will be in order of the 
orbits from the innermost to the outermost, following the example of the sample input hence it worked for that
exampl. As we can simply keep appending the list of the planet to the 
next orbit if the orbitter is orbitting a planet. And then sum up the length of
lists. This can still work but will add more iterations to generate the whole list 
when we can do without it.
'''

if __name__ == "__main__":
    orbits = []
    with open("input.txt", "r") as fp:
        orbits = fp.read().split()
    # Tail Call optimization ?
    print(getPathCount(getUniquePlanets(orbits), generateGraph(orbits)))