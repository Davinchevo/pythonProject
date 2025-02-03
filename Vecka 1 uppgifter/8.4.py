import math

movements = [("UP", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)]

y,x = 0,0

for direction, steps in movements:
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = math.sqrt(x**2 + y**2)

print(round(distance))