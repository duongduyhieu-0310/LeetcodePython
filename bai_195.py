with open('file.txt', 'r') as file:
    lines = file.readlines()
    if len(lines) >= 10:
        print(lines[9])