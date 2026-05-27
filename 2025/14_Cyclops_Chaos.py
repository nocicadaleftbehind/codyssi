import numpy

grid = []
with open("14_Cyclops_Chaos_input.txt") as f:
    for line in f:
        grid.append(list(map(int, line.split())))
grid = numpy.array(grid)

def safest_line(grid):
    return min(grid.sum(axis=0).min(), grid.sum(axis=1).min())

print("PART 1")
print(safest_line(grid))

def safest_path_dynamic(grid, target):
    target = (target[0] - 1, target[1] - 1)
    best_path = numpy.zeros_like(grid)
    
    best_path[0, 0] = grid[0, 0]

    for i in range(1, len(grid[0])):
        best_path[0, i] = best_path[0, i -1] + grid[0, i]
    for i in range(1, len(grid)):
        best_path[i, 0] = best_path[i -1, 0] + grid[i, 0]
    
    for row in range(1, len(best_path)):
        for col in range(1, len(best_path[0])):
            best_path[row][col] = min(best_path[row - 1, col], best_path[row, col - 1]) + grid[row][col]

    return best_path[target]

print("PART 2")
print(safest_path_dynamic(grid, target=(15,15)))

print("PART 3")
print(safest_path_dynamic(grid, target=(len(grid),len(grid[0]))))