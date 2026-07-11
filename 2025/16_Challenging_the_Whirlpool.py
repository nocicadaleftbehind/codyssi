import copy
import re

import numpy

grid = []
instructions = []
actions = []
with open("16_Challenging_the_Whirlpool_input.txt") as f:
    paragraph = 1
    for line in f:
        if line == "\n":
            paragraph += 1
            continue
        if paragraph == 1:
            numbers = list(map(int, line.split()))
            grid.append(numbers)
        if paragraph == 2:
            instructions.append(line.strip())
        if paragraph == 3:
            actions.append(line.strip())
    grid = numpy.array(grid)

operations = {
    "ADD": lambda x, y: x + y,
    "SUB": lambda x, y: x - y,
    "MULTIPLY": lambda x, y: x * y,
}


def apply_instructions(grid, instructions):
    grid = copy.deepcopy(grid)
    for instruction in instructions:
        if m := re.match(r"SHIFT COL (\d+) BY (\d+)", instruction):
            col_num = int(m.group(1))
            amount = int(m.group(2))
            grid[:, col_num - 1] = numpy.roll(grid[:, col_num - 1], amount)
        elif m := re.match(r"SHIFT ROW (\d+) BY (\d+)", instruction):
            row_num = int(m.group(1))
            amount = int(m.group(2))
            grid[row_num - 1, :] = numpy.roll(grid[row_num - 1, :], amount)
        elif m := re.match(r"(.+) (\d+) ROW (\d+)", instruction):
            opcode = m.group(1)
            amount = int(m.group(2))
            row_num = int(m.group(3))
            grid[row_num - 1, :] = operations[opcode](grid[row_num - 1, :], amount) % 1073741824
        elif m := re.match(r"(.+) (\d+) COL (\d+)", instruction):
            opcode = m.group(1)
            amount = int(m.group(2))
            col_num = int(m.group(3))
            grid[:, col_num - 1] = operations[opcode](grid[:, col_num - 1], amount) % 1073741824
        elif m := re.match(r"(.+) (\d+) ALL", instruction):
            opcode = m.group(1)
            amount = int(m.group(2))
            grid = operations[opcode](grid, amount) % 1073741824
        else:
            print("Error")
            print(instruction)

    row_max = max(grid.sum(axis=0))
    col_max = max(grid.sum(axis=1))
    return max(row_max, col_max)


def get_control_flow(instructions, actions, only_one_loop):
    instructions = copy.copy(instructions)
    execution_flow = []
    while len(instructions) > 0:
        for action in actions:
            if len(instructions) == 0:
                break
            if action == "TAKE":
                continue
            elif action == "CYCLE":
                instructions = instructions[1:] + [instructions[0]]
            elif action == "ACT":
                execution_flow.append(instructions[0])
                instructions = instructions[1:]
        if only_one_loop:
            break

    return execution_flow


print("PART 1")
print(apply_instructions(grid, instructions))

print("PART 2")
effective_instructions = get_control_flow(instructions, actions, only_one_loop=True)
print(apply_instructions(grid, effective_instructions))

print("PART 3")
effective_instructions = get_control_flow(instructions, actions, only_one_loop=False)
print(apply_instructions(grid, effective_instructions))
