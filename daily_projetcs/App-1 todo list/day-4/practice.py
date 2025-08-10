todos = []

while True:
    user = input("type add show edit exit : ")
    user.strip()

    match user:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo.capitalize())

        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter number to edit : "))
            number = number -1
            new_todo= input("enter new todo")
            todos[number] = new_todo
        case 'exit':
            break
