with open("input.txt", "r") as f:
    data = f.readlines()
    data = [int(line.rstrip()) for line in data]

previous_depth = 0
increase_counter = 0
iteration_counter = 0

for depth in data:
    current_depth = sum(data[iteration_counter:iteration_counter+3])
    if current_depth > previous_depth:
        increase_counter += 1
    previous_depth = current_depth
    iteration_counter += 1
    
#negate the initial increase of depth
increase_counter -= 1
print (increase_counter)