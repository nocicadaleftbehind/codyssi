ranges = []
with open("7_Supplies_in_Surplus_input.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        for pile in line.split(" "):
            min_r, max_r = pile.split("-")
            ranges.append((int(min_r), int(max_r)))

def range_size(a, b):
    return b - a + 1

total = 0
for min_r, max_r in ranges:
    total += range_size(min_r, max_r)

print("PART 1")
print(total)

def combined_size(range_1, range_2):
    min_1 = range_1[0]
    max_1 = range_1[1]
    min_2 = range_2[0]
    max_2 = range_2[1]

    overlap = max(0, range_size(max(min_1, min_2), min(max_1, max_2)))
    return range_size(min_1, max_1) + range_size(min_2, max_2) - overlap

total = 0
for range_1, range_2 in zip(ranges[::2], ranges[1::2]):
    total += combined_size(range_1, range_2)
print("PART 2")
print(total)

def complete_combine(ranges):
    ranges = list(sorted(ranges, key=lambda r: r[0]))
    
    merged = []
    current = ranges[0]
    for start, end in ranges:
        if start > current[1]:
            merged.append(current)
            current = [start, end]
        if end <= current[1]:
            continue
        current = [current[0], end]
                
    merged.append(current)
    return merged

max_size = 0
for line_1 in range(len(ranges)//2 - 1):
    combined_ranges = complete_combine(ranges[line_1 * 2:line_1 * 2 + 2] + ranges[line_1 * 2 + 2:line_1 * 2 + 4])
    size = sum(range_size(*r) for r in combined_ranges)
    max_size = max(max_size, size)
print("PART 3")
print(max_size)
