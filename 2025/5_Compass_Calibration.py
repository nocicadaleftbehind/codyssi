offsets = []
signs = []
with open("5_Compass_Calibration_input.txt") as f:
    lines = f.readlines()
    for line in lines[:-1]:
        offsets.append(int(line))
    signs = list(lines[-1])

signed_offsets = [offsets[0]] + [-num  if sign == "-" else num for num, sign in zip(offsets[1:], signs)]

print("PART 1")
print(sum(signed_offsets))

signed_offsets = [offsets[0]] + [-num  if sign == "-" else num for num, sign in zip(offsets[1:], reversed(signs))]

print("PART 2")
print(sum(signed_offsets))

paired_offsets = [10*a + b for a, b in zip(offsets[::2], offsets[1::2])]
signed_offsets = [paired_offsets[0]] + [-num  if sign == "-" else num for num, sign in zip(paired_offsets[1:], reversed(signs))]

print("PART 3")
print(sum(signed_offsets))
