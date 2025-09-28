
while True:
    user = input("type add show edit delete exit : ")
    user.strip()

    if 'add' in user or 'new' in user:
        todo = user[4:]

        with open('todo_list9.txt','r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('todo_list9.txt','w') as file:
            file.writelines(todos)


    elif 'show' in user:
        with open('todo_list9.txt','r') as file:
            todos = file.readlines()

        for index, item in enumerate (todos):
            item = item.strip('\n')
            row= f"{index +1}: {item}"
            print(row)

    elif 'edit' in user:
        number = int(user[5:])
        number = number -1

        with open('todo_list9.txt','r') as file:
            todos = file.readlines()

        new_todo= input("enter new todo : ")
        todos[number] = new_todo + '\n'

        with open('todo_list9.txt','w') as file:
            file.writelines(todos)

    elif 'delete' in user:
        number = int(user [7:])

        with open('todo_list9.txt','r') as file:
            todos = file.readlines()

        index = number -1
        remove = todos[index]

        todos.pop(number-1)
        message = f" todo {remove} was deleted successfully"

        print(message)

        with open('todo_list9.txt','w') as file:
            file.writelines(todos)

    elif 'exit' in user:
            break
    else:
        print("Command is invalid")

print('bye')
