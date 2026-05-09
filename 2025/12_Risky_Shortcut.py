import re

data = []
with open("12_Risky_Shortcut_input.txt") as f:
    data = [l.replace("\n", "") for l in f.readlines()]

def is_alphabetical(char):
    if char.isalpha():
        return True
    else:
        return False

total = 0
for line in data:
    total += sum(map(is_alphabetical, line))
print("PART 1")
print(total)

def fully_reduce(line, with_hyphen):
    right_pattern = r"[a-z]\d"
    left_pattern = r"\d[a-z]"
    if with_hyphen:
        right_pattern = r"[a-z-]\d"
        left_pattern = r"\d[a-z-]"
    
    prev = line
    while True:
        line = re.sub(right_pattern, "", line)
        line = re.sub(left_pattern, "", line)
        if prev == line:
            return line
        prev = line
        
total = 0
for line in data:
    reduced_line = fully_reduce(line, with_hyphen=True)
    total += len(reduced_line) 
    
print("PART 2")
print(total)


total = 0
for line in data:
    reduced_line = fully_reduce(line, with_hyphen=False)
    total += len(reduced_line)

print("PART 3")
print(total)