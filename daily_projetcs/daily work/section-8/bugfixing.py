with open("file.txt", 'r') as file:
    length= len(file.read())
    print(file.read())
    print(length)