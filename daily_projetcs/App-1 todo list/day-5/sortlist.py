my_list = ['Z', 'I', 'A', 'B', 'G', 'W', 'E', 'H']
my_list.sort()

for index, item in enumerate(my_list):
    row = f"{index +1}.{item.capitalize()}"
    print(row)

print( "the List is sorted in ascending order")


my_lists = ['Z', 'I', 'A', 'B', 'G', 'W', 'E', 'H']
my_list.sort(reverse=True)

for index, item in enumerate(my_lists):
    row = f"{index +1}.{item.capitalize()}"
    print(row)

print( "the List is sorted in descending order")