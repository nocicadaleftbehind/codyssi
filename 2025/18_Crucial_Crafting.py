from collections import namedtuple

import numpy
import re

Item = namedtuple("Item", ["id", "name", "quality", "cost", "materials"])

items = {}
with open("18_Crucial_Crafting_input.txt") as f:
    for line in f:
        m = re.match(r"(\d+) (.+) \| Quality : (\d+), Cost : (\d+), Unique Materials : (\d+)", line)
        if m:
            items[int(m.group(1))] = Item(int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        else:
            print("Cannot parse line", line)

def sort_materials(materials):
    return list(sorted(materials.values(), key= lambda m: (m.quality, m.cost), reverse=True))

def get_highest_quality_materials(materials):
    sorted_materials = sort_materials(materials)
    sorted_materials = sorted_materials[:5]
    return sum([m.materials for m in sorted_materials])

def max_tuple(t1, t2):
    if t1[0] > t2[0]:
        return t1
    elif t1[0] == t2[0] and t1[1] < t2[1]:
        return 1
    return t2

def find_optimal_combination(sorted_materials, target):
    num_materials = len(sorted_materials)
    partial_solutions = numpy.zeros((num_materials + 1, target + 1, 2), dtype=numpy.int64)

    for i in range(target + 1):
        partial_solutions[0, i] = 0
    for i in range(num_materials + 1):
        partial_solutions[i, 0] = 0
    for i in range(1, num_materials + 1):
        for j in range(1, target + 1):
            material = sorted_materials[i]
            w_i = material.cost
            v_i = (material.quality, material.materials)

            if w_i > j:
                partial_solutions[i, j] = partial_solutions[i - 1, j]
            else:
                partial_solutions[i, j] = max_tuple(partial_solutions[i - 1, j], partial_solutions[i - 1, j - w_i] + v_i)

    best_quality = partial_solutions[-1, -1][0]
    best_unique_materials = partial_solutions[-1, -1][1]
    return best_quality * best_unique_materials

print("PART 1")
print(get_highest_quality_materials(items))

print("PART 2")
print(find_optimal_combination(items, target=30))

print("PART 3")
print(find_optimal_combination(items, target=300))
