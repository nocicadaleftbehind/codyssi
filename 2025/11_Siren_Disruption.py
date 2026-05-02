import copy

frequencies = [None]
swaps = []
test_freq = None
with open("11_Siren_Disruption_input.txt") as f:
    parse_state = 1
    for line in f:
        if line == "\n":
            parse_state += 1
            continue
        if parse_state == 1:
            frequencies.append(int(line))
        if parse_state == 2:
            swap = tuple(map(int, line.split("-")))
            swaps.append([swap[0], swap[1]])
        if parse_state == 3:
            test_freq = int(line)


def swap_two(f, swaps):
    f = copy.copy(f)
    for a, b in swaps:
        f[a], f[b] = f[b], f[a]
    
    return f

frequencies_2_swapped = swap_two(frequencies, swaps) 
print("PART 1")
print(frequencies_2_swapped[test_freq])


def swap_three(f, swaps):
    f = copy.copy(f)
    for a, b, c in swaps:
        f[a], f[b], f[c] = f[c], f[a], f[b]

    return f

swap_triplets = [(s1[0],s1[1], s2[0]) for (s1,s2) in zip(swaps, swaps[1:] + swaps)]
frequencies_3_swapped = swap_three(frequencies, swap_triplets)
print("PART 2")
print(frequencies_3_swapped[test_freq])

def swap_blocks(f, swaps):
    f = copy.copy(f)
    for a, b in swaps:
        greater = max(a,b)
        lesser = min(a,b)
        block_length = min(greater - lesser, len(f) - greater)
        for j in range(block_length):
            f[a + j], f[b + j] = f[b + j], f[a + j] 

    return f

print("PART 3")
frequencies_block_swapped = swap_blocks(frequencies, swaps)
print(frequencies_block_swapped[test_freq])
