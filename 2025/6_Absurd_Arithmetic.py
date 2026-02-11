import re

numbers = []
with open("6_Absurd_Arithmetic_input.txt") as f:
    lines = f.readlines()
    functions = lines[:3]
    for line in lines[4:]:
        numbers.append(int(line))

def apply_function(function_string, number):
    m = re.search(r"RAISE TO THE POWER OF (\d+)", function_string)
    if m:
        return number ** (int(m.group(1)))
    m = re.search(r"MULTIPLY (\d+)", function_string)
    if m:
        return number * (int(m.group(1)))
    m = re.search(r"ADD (\d+)", function_string)
    if m:
        return number + int(m.group(1))
    return None

def reverse_function(function_string, number):
    m = re.search(r"RAISE TO THE POWER OF (\d+)", function_string)
    if m:
        return int(number ** (1/int(m.group(1))))
    m = re.search(r"MULTIPLY (\d+)", function_string)
    if m:
        return number // int(m.group(1))
    m = re.search(r"ADD (\d+)", function_string)
    if m:
        return number - int(m.group(1))
    return None


def convert_to_pecunia(price):
    for func in reversed(functions):
        price = apply_function(func, price)
    return price

def convert_from_pecunia(price):
    for func in functions:
        price = reverse_function(func, price)
    return price

median_price = sorted(numbers)[len(numbers) // 2]

print("PART 1")
print(convert_to_pecunia(median_price))

print("PART 2")
even_price_sum = sum([price for price in numbers if price % 2 == 0])
total = convert_to_pecunia(even_price_sum)
print(total)

print("PART 3")
limit = 15000000000000
price = convert_from_pecunia(limit)
print(max([p for p in numbers if p <= price]))
