def function(string, width):
    spaces = "a" *int((width / 2))
    return spaces + string

print(function("Hi there", 80))