readings = []
with open("2_Sensors_and_Circuits_input.txt") as f:
    for line in f:
        line = line.strip()
        readings.append(line == "TRUE")
        
print("PART 1")
print(sum([i+1 for i, l in enumerate(readings) if l]))

def layer(readings):
    pairs = zip(readings[::2], readings[1::2])
    
    gate_outputs = []
    for gate_index, inputs in enumerate(pairs):
        if gate_index % 2 == 0:
            gate_output = inputs[0] and inputs[1]
        else:
            gate_output = inputs[0] or inputs[1]
        gate_outputs.append(gate_output)
    
    return gate_outputs

print("PART 2")
print(sum(layer(readings)))

num_true_gates = sum(readings)
while len(readings) > 1:
    readings = layer(readings)
    num_true_gates += sum(readings)

print("PART 3")
print(num_true_gates)