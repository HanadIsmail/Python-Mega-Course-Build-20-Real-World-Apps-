def get_todos():
    with open('todo_list11.txt', 'r') as file:
        todos = file.readlines()

    return todos

while True:
    user = input("type add show edit delete exit : ")
    user.strip()

    if user.startswith('add') :
        todo = user[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        with open('todo_list10.txt','w') as file:
            file.writelines(todos)


    elif user.startswith('show') :
        todos = get_todos()

        for index, item in enumerate (todos):
            item = item.strip('\n')
            row= f"{index +1}: {item}"
            print(row)

    elif user.startswith('edit') :
        try:
            number = int(user[5:])
            number = number -1

            todos = get_todos()

            new_todo= input("enter new todo : ")
            todos[number] = new_todo + '\n'

            with open('todo_list10.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid Command")
            continue

    elif user.startswith('delete') :
        try:
            number = int(user [7:])

            todos = get_todos()

            index = number -1
            remove = todos[index]

            todos.pop(number-1)
            message = f" todo {remove} was deleted successfully"

            print(message)

            with open('todo_list10.txt','w') as file:
                file.writelines(todos)
        except IndexError:
            print("That number is out of range")
            continue

    elif user.startswith('exit') :
            break
    else:
        print("Command is invalid")

print('bye')
