with open("input.txt", "r") as f:
    data = f.readlines()
    data = [int(line.rstrip()) for line in data]

previous_depth = 0
increase_counter = 0

for depth in data:
    if depth > previous_depth:
        increase_counter += 1
    previous_depth = depth
#negate the initial increase of depth
increase_counter -= 1
print(increase_counter)