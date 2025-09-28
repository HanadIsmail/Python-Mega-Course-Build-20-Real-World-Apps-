#Define a function that:

#(1) takes a list as an argument

#(2) returns the average value of the list items.

#For example, if I called your function with foo([10, 20, 30, 40]) it should return 25 which is the average of the numbers of the list.

def average(mylist):
    return sum(mylist) / len(mylist)

average([10,20,30,40])
print(average([10,20,30,40]))