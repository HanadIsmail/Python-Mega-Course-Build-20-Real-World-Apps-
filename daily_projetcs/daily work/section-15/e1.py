import glob

myfiles = glob.glob('*.txt')

for myfile in myfiles:
    with open(myfile,'r') as file:
        print(file.read())