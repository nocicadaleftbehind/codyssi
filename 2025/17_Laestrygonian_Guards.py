import re
from collections import defaultdict
import heapq

paths = defaultdict(list)
with open("17_Laestrygonian_Guards_input.txt") as f:
    for line in f:
        m = re.match(r"(.+) -> (.+) \| (\d+)", line)
        if m:
            paths[m.group(1)].append((m.group(2), int(m.group(3))))

def find_all_paths(paths, override_path_length=False):
    path_lengths = {"STT": 0}
    queue = [(0, ["STT"])]
    while queue:
        length, current_path = queue.pop(0)
        current = current_path[-1]
        path_lengths[current] = length
        for neighbor, distance in paths[current]:
            if override_path_length:
                distance = 1
            if neighbor not in path_lengths.keys():
                heapq.heappush(queue, (length + distance, current_path + [neighbor]))
    return path_lengths

def product_longest_paths(paths, override_path_length=False):
    path_lengths = find_all_paths(paths, override_path_length)
    paths_lengths = list(sorted(path_lengths.values()))
    return paths_lengths[-1] * paths_lengths[-2] * paths_lengths[-3]

def find_cycles(paths):
    cycles = []
    queue = [(0, ["STT"])]
    while queue:
        length, current_path = queue.pop(0)
        current = current_path[-1]
        for neighbor, distance in paths[current]:
            if neighbor in current_path:
                cycles.append(current_path + [neighbor])
            else:
                heapq.heappush(queue, (length + distance, current_path + [neighbor]))
    
    return longest_cycle(cycles)

def longest_cycle(cycles):
    max_length = 0
    for cycle in cycles:
        start = cycle.index(cycle[-1])
        cycle = cycle[start:]
        length = 0
        for start, end in zip(cycle, cycle[1:]):
            for neighbor, distance in paths[start]:
                if neighbor == end:
                    length += distance
        max_length = max(max_length, length)
    return max_length

print("PART 1")
print(product_longest_paths(paths, override_path_length=True))

print("PART 2")
print(product_longest_paths(paths))

print("PART 3")
print(find_cycles(paths))
