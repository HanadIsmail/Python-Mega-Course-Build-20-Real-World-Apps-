todos = []

while True:
    user = input("type add show exit : ")
    user.strip()

    match user:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo.capitalize())

        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

list = ['1','2','3','4']
for item in list:
    if int (item) % 2 == 0:
        print('even number')
    else:
        print('odd number')