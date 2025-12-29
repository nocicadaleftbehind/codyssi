lines = []
with open("3_Unformatted_Readings_input.txt") as f:
    for line in f:
        lines.append(line.replace("\n", "").split(" "))

base_sum = 0
for line in lines:
    base_sum += int(line[1])

print("PART 1")
print(base_sum)

converted_sum = 0
for line in lines:
    converted_sum += int(line[0], int(line[1]))

print("PART 2")
print(converted_sum)

base_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#"
base_65_string = ""
while converted_sum > 0:
    base_65_string = base_digits[converted_sum % 65] + base_65_string 
    converted_sum //= 65

print("PART 3")
print(base_65_string)