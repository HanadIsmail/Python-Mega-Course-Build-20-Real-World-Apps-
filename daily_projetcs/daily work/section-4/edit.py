todos = []

while True:
    user = input("Type add, show or display, edit, exit : ")
    user.strip()

    match user:
        case 'add':
            todo = input("enter a todo : ")
            todos.append(todo)
        case 'show' | 'display':
            for i in todos:
                print(i)
        case 'edit':
            number = int(input("Enter a number to edit : "))
            number = number -1
            new_todo = input("Enter new to do :")
            todos[number] = new_todo
            print(new_todo)
        case 'exit':
            break

print("bye!")














