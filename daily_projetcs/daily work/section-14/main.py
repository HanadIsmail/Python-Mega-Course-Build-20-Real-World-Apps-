#from function import get_todos , write_todos
import function

while True:
    user = input("type add show edit delete exit : ")
    user.strip()

    if user.startswith('add') :
        todo = user[4:]

        todos = function.get_todos()

        todos.append(todo + "\n")

        function.write_todos(todos)

    elif user.startswith('show') :
        todos = function.get_todos()

        for index, item in enumerate (todos):
            item = item.strip('\n')
            row= f"{index +1}: {item}"
            print(row)

    elif user.startswith('edit') :
        try:
            number = int(user[5:])
            number = number -1

            todos = function.get_todos()

            new_todo= input("enter new todo : ")
            todos[number] = new_todo + '\n'

            function.write_todos(todos)
        except ValueError:
            print("Invalid Command")
            continue

    elif user.startswith('delete') :
        try:
            number = int(user [7:])

            todos = function.get_todos()

            index = number -1
            remove = todos[index]

            todos.pop(number-1)
            message = f" todo {remove} was deleted successfully"

            print(message)

            function.write_todos(todos)
        except IndexError:
            print("That number is out of range")
            continue

    elif user.startswith('exit') :
            break
    else:
        print("Command is invalid")

print('bye')
