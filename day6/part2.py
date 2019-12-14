import os

'''Using the concept of lowest common ancestor,
find the invidual paths of YOU and SAN

Start travelling from COM to YOU, SAN simultaneously until
there are no common paths, this is the point where both paths
merge and the path YOU will take to SAN.
'''
def getUniquePlanets(orbits):
    return list(["YOU", "SAN"])

def generateGraph(orbits):
    orbit_map = {}
    for orbit in orbits:
        center, orbiter = orbit.split(")")
        orbit_map[orbiter] = center

    return orbit_map
        
def getPathCount(planets, orbits):
    paths = {}
    for pls in planets:
        planet = pls
        paths[pls] = []
        while planet in orbits:
            planet = orbits[planet]
            paths[pls].append(planet)

    you_path = paths['YOU'][::-1]
    san_path = paths['SAN'][::-1]

    print(len(you_path), len(san_path))
    hop = 0

    i, j = -1, -1
    while i < len(you_path) and j < len(san_path):
        if you_path[i+1] != san_path[j+1]:
            print("Common till ==> " + you_path[i])
            break
        i += 1
        j += 1
        # print("Same: YOU {},{} SAN {},{}".format(i, you_path[i], j, san_path[j]))   

    print(i, len(you_path[i:]) - 1) 
    print(j, len(san_path[j:]) - 1)

    return len(you_path[i:]) - 1 + len(san_path[j:]) - 1

if __name__ == "__main__":
    orbits = []
    with open("input.txt", "r") as fp:
        orbits = fp.read().split()
    # Tail Call optimization ?
    print(getPathCount(getUniquePlanets(orbits), generateGraph(orbits)))