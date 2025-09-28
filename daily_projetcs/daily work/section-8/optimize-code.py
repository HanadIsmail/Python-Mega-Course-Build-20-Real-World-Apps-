
while True:
    user = input("type add show edit delete exit : ")
    user.strip()

    match user:
        case 'add':
            todo = input("Enter a todo : ") + '\n'

            with open('todo_list.txt','r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todo_list.txt','w') as file:
                file.writelines(todos)


        case 'show':
            with open('todo_list.txt','r') as file:
                todos = file.readlines()

            for index, item in enumerate (todos):
                item = item.strip('\n')
                row= f"{index +1}: {item}"
                print(row)

        case 'edit':
            number = int(input("Enter number to edit : "))
            number = number -1

            with open('todo_list.txt','r') as file:
                todos = file.readlines()

            new_todo= input("enter new todo : ")
            todos[number] = new_todo + '\n'

            with open('todo_list.txt','w') as file:
                file.writelines(todos)

        case 'delete':
            number = int(input("Enter number to delete : "))

            with open('todo_list.txt','r') as file:
                todos = file.readlines()

            index = number -1
            remove = todos[index]

            todos.pop(number-1)
            message = f" todo {remove} was deleted successfully"

            print(message)

            with open('todo_list.txt','w') as file:
                file.writelines(todos)

        case 'exit':
            break


