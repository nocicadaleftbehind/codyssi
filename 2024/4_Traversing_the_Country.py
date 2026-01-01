import collections
import re

connections = collections.defaultdict(list)
with open("4_Traversing_the_Country_input.txt") as f:
    for line in f:
        m = re.match("(.*) <-> (.*)", line)
        if m:
            orig, dest = m.group(1), m.group(2)
            connections[orig].append(dest)
            connections[dest].append(orig)


print("PART 1")
print(len(connections.keys()))

reachable = dict()
queue = [(0, "STT")]
while len(queue) > 0:
    path_length, current_state = queue.pop(0)
    if current_state in reachable.keys():
        if reachable[current_state] < path_length:
            continue
    
    reachable[current_state] = path_length
    for connected in connections[current_state]:
        queue.append((path_length + 1, connected))

reachable_in_3 = {k:v for (k,v) in reachable.items() if v <= 3}

print("PART 2")
print(len(reachable_in_3))

print("PART 3")
print(sum(reachable.values()))
