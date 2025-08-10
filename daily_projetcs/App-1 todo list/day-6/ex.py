file = open("essay.txt",'r')
content = file.read()
file.close()

print(f"The file contains {len(content)}.characters.")