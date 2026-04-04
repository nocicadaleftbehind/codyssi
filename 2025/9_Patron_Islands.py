islands = []
with open("9_Patron_Islands_input.txt") as f:
    for line in f:
        islands.append(list(map(int, line.strip("()\n").split(","))))

def manhattan_distance(target, origin):
    return abs(target[0] - origin[0]) + abs(target[1] - origin[1])

def calc_distances(islands, origin):
    return [manhattan_distance(target, origin) for target in islands if target != origin]

def next_island_id(islands, origin):
    distances = calc_distances(islands, origin)
    closest_islands = [i for i in range(len(islands)) if distances[i] == min(distances)]
    closest_islands.sort()
    closest_island = closest_islands[0]

    return closest_island

distances = calc_distances(islands, (0,0))

print("PART 1")
print(max(distances) - min(distances))

closest = next_island_id(islands, (0, 0))
closest_distances = calc_distances(islands, islands[closest])

print("PART 2")
print(min(closest_distances))

total_length = 0
current = [0,0]
while len(islands) > 0:
    closest = next_island_id(islands, current)
    total_length += manhattan_distance(islands[closest], current)
    current = islands.pop(closest)

print("PART 3")
print(total_length)