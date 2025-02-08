def center(string, width):
    spaces= " " * (int(width/2) - len(string)/2)
    return spaces + string

print(center("Hejsan", 80))