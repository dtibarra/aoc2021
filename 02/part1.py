with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]

horizontal = 0
depth = 0

for instruction in data:
    direction = instruction.split(" ")[0]
    distance = int(instruction.split(" ")[1])
    match direction:
        case "down":
            depth += distance
        case "up":
            depth -= distance
        case "forward":
            horizontal += distance

print(horizontal*depth)