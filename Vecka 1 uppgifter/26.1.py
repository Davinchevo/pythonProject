def console_center(string, width):
    spaces = " " * int((width / 2) - (len(string)/2))
    return spaces + string
 
def main():
    print(console_center("Hi there", 180))
            
if __name__ == '__main__':
    main()