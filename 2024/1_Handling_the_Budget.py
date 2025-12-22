prices = []
with open("1_Handling_the_Budget_input.txt") as f:
    for line in f:
        prices.append(int(line))

print("PART 1")
print(sum(prices))

NUM_ITEMS_FREE = 20
sorted_prices = list(sorted(prices))

print("PART 2")
print(sum(sorted_prices[:-NUM_ITEMS_FREE]))

positive_sum = sum(prices[::2])
negative_sum = sum(prices[1::2])

print("PART 3")
print(positive_sum - negative_sum)
