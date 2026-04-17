with open("10_Lotus_Scramble_input.txt") as f:
    log = f.read().strip()

def only_uncorrupted(c):
    return c.islower() or c.isupper() 

print("PART 1")
print(sum(map(only_uncorrupted, log)))

def char_values(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    if c.isupper():
        return ord(c) - ord("A") + 27
    return 0

print("PART 2")
print(sum(map(char_values, log)))

values = []
for c in log:
    val = 0
    if c.islower():
        val = ord(c) - ord("a") + 1
    elif c.isupper():
        val = ord(c) - ord("A") + 27
    else:
        val = values[-1] * 2 - 5
        val = (val - 1) % 52 + 1
    values.append(val)

print("PART 3")
print(sum(values))
    
    