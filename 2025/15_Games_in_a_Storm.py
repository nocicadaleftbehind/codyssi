import math
from string import ascii_uppercase, ascii_lowercase, digits
from typing import Any

numbers = []
with open("15_Games_in_a_Storm_input.txt") as f:
    for line in f:
        string, base = line.split()
        numbers.append((string, int(base)))

def parse_string_with_arbitrary_base(s, base):
    total = 0
    for c in s:
        total *= base
        total += char_value(c, total)
    return total


def char_value(c):
    if "0" <= c <= "9":
        return int(c)
    elif "A" <= c <= "Z":
        return ord(c) - ord("A") + 10
    return ord(c) - ord("a") + 36


parsed_numbers = [parse_string_with_arbitrary_base(s, base) for s, base in numbers]

print("PART 1")
print(max(parsed_numbers))

def num_to_string(num):
    s = ""
    digitschars = digits + ascii_uppercase + ascii_lowercase + "!@#$%^"
    while num > 0:
        last_digit = num % 68
        s = digitschars[last_digit] + s 
        num //= 68
    return s

total_sum = sum(parsed_numbers)
print("PART 2")
print(num_to_string(total_sum))

print("PART 3")
print(math.floor(total_sum**(1/4)) + 1)