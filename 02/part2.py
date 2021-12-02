with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]

horizontal = 0
depth = 0
aim = 0

for instruction in data:
    direction = instruction.split(" ")[0]
    distance = int(instruction.split(" ")[1])
    match direction:
        case "down":
            aim += distance
        case "up":
            aim -= distance
        case "forward":
            horizontal += distance
            depth += (aim * distance)

print(horizontal*depth)