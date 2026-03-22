import itertools

messages = []
with open("8_Aeolian_Transmissions_input.txt") as f:
    for line in f:
        messages.append(line.strip())
    
def line_memory(line):
    line = map(ord, line)
    line = [c - ord("A") + 1 if ord("A") <= c <= ord("Z") else c - ord("0") for c in line]
    return sum(line)

print("PART 1")
print(sum([line_memory(message) for message in messages]))

def compress_lossy(line):
    line_length = len(line)
    chars_kept = line_length // 10
    return line[:chars_kept] + str(line_length - 2 * chars_kept) + line[-chars_kept:]

print("PART 2")
print(sum([line_memory(compress_lossy(message)) for message in messages]))

def compress_lossless(line):
    s = ""
    for char, group in itertools.groupby(line):
        s += f"{len([_ for _ in group])}{char}"
    return s

print("PART 3")
print(sum([line_memory(compress_lossless(message)) for message in messages]))
